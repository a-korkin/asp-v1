from typing import List
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

    class Config: 
        orm_mode = True

class User(UserBase):
    id: str

    class Config:
        orm_mode = True

    