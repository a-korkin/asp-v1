import json
import traceback
from typing import Optional
from uuid import UUID
from fastapi import APIRouter, HTTPException
from fastapi.openapi.models import Response
from fastapi.params import Cookie, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session
from api.config import settings
from api.models.user import User
from api.crud import crud_user
from api.schemas.user import UserSchema
from api.utils import get_db, create_token, verify_password, get_password_hash, get_current_user, check_refresh_token
from datetime import timedelta

router = APIRouter()  
   
@router.get("/secret")    
async def secret(current_user: User = Depends(get_current_user)):
    return {"m": current_user.username}

@router.get("/token/{tok}")
async def index(tok: str, db: Session = Depends(get_db)):
    print(get_current_user(token=tok, secret_key=settings.JWT_ACCESS_TOKEN_SECRET_KEY, db=db))
    return {"message": "fucker"}

@router.post("/login")    
async def login(user: UserSchema, db: Session = Depends(get_db)):
    db_user: User = crud_user.fetch_user_by_name(db, user.username)

    if not db_user:
        raise HTTPException(status_code=403, detail="access denied")
    
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=403, detail="access denied")
      
    access_token = create_token({"user": user.username}, settings.JWT_ACCESS_TOKEN_SECRET_KEY, timedelta(minutes=15))
    refresh_token = create_token({"user": user.username}, settings.JWT_REFRESH_TOKEN_SECRET_KEY, timedelta(days=10))
    
    try:
        db_user.refresh_token = refresh_token
        crud_user.update_user(db, db_user)
    except:
        print(traceback.format_exc())
    content = {"accessToken": access_token, "user": dict(user)}
    response = JSONResponse(content=content)
    response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
    return response

@router.post("/logout")    
async def logout():
    content = {"message": "logged out"}
    response = JSONResponse(content=content)
    response.delete_cookie(key="refresh_token")
    return response

@router.get("/refresh")    
async def refresh(refresh_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):
    try:
        user = check_refresh_token(token=refresh_token, db=db)
        
        access_token = create_token({"user": user.username}, settings.JWT_ACCESS_TOKEN_SECRET_KEY, timedelta(minutes=15))
        _refresh_token = create_token({"user": user.username}, settings.JWT_REFRESH_TOKEN_SECRET_KEY, timedelta(days=10))
        
        user.refresh_token = _refresh_token
        crud_user.update_user(db, user)
        content = {"accessToken": access_token, "user": {"username": user.username, "password": user.password}}
        response = JSONResponse(content=content)
        response.set_cookie(key="refresh_token", value=_refresh_token, httponly=True)
        return response
    except:
        print(traceback.format_exc())


@router.post("/users", status_code=201)
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    db_user = crud_user.fetch_user_by_name(db=db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="user already exists")

    user.password = get_password_hash(user.password)
    db_user = crud_user.create_user(db, user)
    return {"message": "user created"}

@router.get("/users/{user_id}", status_code=200)    
async def get_user(user_id: UUID, db: Session = Depends(get_db)):
    db_user = crud_user.fetch_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="user not found")
    
    return db_user

@router.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: UUID, db: Session = Depends(get_db)):
    db_user = crud_user.fetch_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="user not found")
    
    crud_user.drop_user(db=db, user=db_user)
    return {"message": "user deleted"}
