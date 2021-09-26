import traceback
from uuid import UUID
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from jose import jwt
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session
from api.config import settings
from api.models.user import User
from api.crud import crud_user
from api.dependencies import get_db
from passlib.context import CryptContext
from api.schemas.user import UserSchema

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(pwd, hash):
    return pwd_context.verify(pwd, hash)

def get_password_hash(pwd):
    return pwd_context.hash(pwd)    

@router.get("/")
async def index():
    return {"message": "fucker"}

@router.post("/login")    
async def login(user: UserSchema):
    access_token = jwt.encode({"user": user.username}, settings.JWT_ACCESS_TOKEN_SECRET_KEY, algorithm="HS256")
    refresh_token = jwt.encode({"user": user.username}, settings.JWT_REFRESH_TOKEN_SECRET_KEY, algorithm="HS256")
    content = {"accessToken": access_token}
    response = JSONResponse(content=content)
    response.set_cookie(key="refreshToken", value=refresh_token, httponly=True)
    return response

@router.post("/users", status_code=201)
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    db_user = crud_user.fetch_user_by_name(db=db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="user already exists")

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
