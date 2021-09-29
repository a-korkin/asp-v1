from pydantic.fields import Field
from api.schemas.user import UserBase
from pydantic import BaseModel

class AuthIn(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True

class AuthOut(BaseModel):
    access_token: str
    user: UserBase

    class Config:
        orm_mode = True
