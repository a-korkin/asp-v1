from typing import List
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserDTO(UserBase):
    password: str

    class Config:
        orm_mode = True
    