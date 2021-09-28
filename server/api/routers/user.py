from fastapi import APIRouter
from fastapi.params import Depends
from api.utils import get_current_user
from api.models.user import User

router = APIRouter(prefix="/users")

@router.get("/")
async def get_list(current_user: User = Depends(get_current_user)):
    return {"users": current_user}
