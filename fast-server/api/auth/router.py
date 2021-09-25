from typing import Optional
from fastapi import APIRouter
from fastapi.params import Cookie
from pydantic import BaseModel
from jose import jwt
from fastapi.responses import JSONResponse

class User(BaseModel):
    username: str
    password: str

router = APIRouter()

@router.get("/")
async def index(fucker: Optional[str] = Cookie(None)):
    return {"message": fucker}

@router.post("/login")    
async def login(user: User, fucker: Optional[str] = Cookie(None)):
    token = jwt.encode({"user": user.username}, "SECRET_KEY", algorithm="HS256")
    content = {"accessToken": token}
    response = JSONResponse(content=content)
    response.set_cookie(key="fucker", value="mother")
    return response
