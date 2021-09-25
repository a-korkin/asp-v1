from typing import Optional
from fastapi import APIRouter
from fastapi.params import Cookie, Depends
from pydantic import BaseModel
from jose import jwt
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session
from api.config import settings
from api.db import SessionLocal
from . import models, crud
import traceback

class UserSchema(BaseModel):
    username: str
    password: str

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

router = APIRouter()

@router.get("/")
async def index(fucker: Optional[str] = Cookie(None)):
    return {"message": fucker}

@router.post("/login")    
async def login(user: UserSchema):
    access_token = jwt.encode({"user": user.username}, settings.jwt_access_token_secret_key, algorithm="HS256")
    refresh_token = jwt.encode({"user": user.username}, settings.jwt_refresh_token_secret_key, algorithm="HS256")
    content = {"accessToken": access_token}
    response = JSONResponse(content=content)
    response.set_cookie(key="refreshToken", value=refresh_token, httponly=True)
    return response

@router.post("/users")
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    user_d = models.User(username=user.username, password=user.password)
    try:
        db_user = crud.create_user(db=db, user=user_d)
    except Exception:
        print(traceback.format_exc())
    return {"message": "pooos"}
