from pydantic.fields import Field
from api.schemas.user import UserDTO
from pydantic import BaseModel

class AuthInDTO(BaseModel):
    username: str
    password: str

class AuthOutDTO(BaseModel):
    access_token: str
    user: UserDTO
