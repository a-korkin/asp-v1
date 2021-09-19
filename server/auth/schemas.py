from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password: str
    lastname: str
    firstname: str

class User(UserBase):    
    class Config:
        orm_mode = True
