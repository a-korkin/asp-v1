from typing import Optional
from fastapi import APIRouter
from fastapi.params import Cookie
from pydantic import BaseModel
from jose import jwt
from fastapi.responses import JSONResponse
from api.config import settings

class User(BaseModel):
    username: str
    password: str

router = APIRouter()

@router.get("/")
async def index(fucker: Optional[str] = Cookie(None)):
    return {"message": fucker}

@router.post("/login")    
async def login(user: User):
    access_token = jwt.encode({"user": user.username}, settings.jwt_access_token_secret_key, algorithm="HS256")
    refresh_token = jwt.encode({"user": user.username}, settings.jwt_refresh_token_secret_key, algorithm="HS256")
    content = {"accessToken": access_token}
    response = JSONResponse(content=content)
    response.set_cookie(key="refreshToken", value=refresh_token, httponly=True)
    return response
