import traceback
from typing import Optional
from datetime import timedelta
from fastapi import APIRouter, HTTPException, Response
from fastapi.params import Cookie, Depends
from sqlalchemy.orm.session import Session
from api.config import settings
from api.models.user import User
from api.services import user as user_service
from api.schemas.auth import AuthIn, AuthOut
from api.schemas.user import UserBase
from api.utils import get_db, create_token, verify_password, get_password_hash, get_current_user, check_refresh_token

router = APIRouter()  

def get_tokens(user: User, response: Response, db: Session) -> AuthOut:
    access_token = create_token({"user": user.username}, settings.JWT_ACCESS_TOKEN_SECRET_KEY, timedelta(minutes=15))
    refresh_token = create_token({"user": user.username}, settings.JWT_REFRESH_TOKEN_SECRET_KEY, timedelta(days=10))
    try:
        user.refresh_token = refresh_token
        user_service.update_user(db, user)
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
        return AuthOut(access_token=access_token, user=UserBase(username=user.username))
    except:
        print(traceback.format_exc())
   
@router.post("/login", response_model=AuthOut)    
async def login(auth_in: AuthIn, response: Response, db: Session = Depends(get_db)):
    user: User = user_service.fetch_user_by_name(db, auth_in.username)
    if not user:
        raise HTTPException(status_code=403, detail="access denied")
    
    if not verify_password(auth_in.password, user.password):
        raise HTTPException(status_code=403, detail="access denied")

    try:
        resp = get_tokens(user=user, response=response, db=db)
        return resp
    except:  
        raise HTTPException(status_code=403, detail="access denied")

@router.post("/logout")    
async def logout(response: Response, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    current_user.refresh_token = None
    user_service.update_user(db=db, user=current_user)
    response.delete_cookie(key="refresh_token")
    return {"detail": "logged out"}

@router.get("/refresh", response_model=AuthOut)    
async def refresh(response: Response, refresh_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):
    try:
        user = check_refresh_token(token=refresh_token, db=db)
        resp = get_tokens(user=user, response=response, db=db)
        return resp
    except:
        raise HTTPException(status_code=401, detail="unauthorized")
