from fastapi import APIRouter
from fastapi.params import Depends
from api.utils import get_current_user
from api.models.user import User
from api.schemas import user

router = APIRouter(prefix="/users")

@router.get("/")
async def get_list(current_user: User = Depends(get_current_user)):
    user1 = user.UserDTO(username=current_user.username, password=current_user.password)
    user2 = user.UserDTO(username=current_user.username, password=current_user.password)

    users = [user1, user2]
    return users
