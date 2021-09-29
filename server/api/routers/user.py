import traceback
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from api.utils import get_current_user, get_db, get_password_hash
from api.models.user import User
from api.schemas.user import User as UserDTO, UserCreate
import api.services.user as user_service

router = APIRouter(prefix="/users")

def get_user_dict(user: User) -> UserDTO:
    return UserDTO(id = str(user.id), username=user.username)

@router.post("/")
async def create_user(user: UserCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_user = user_service.fetch_user_by_name(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="user already exists")
    user.password = get_password_hash(user.password)
    db_user = user_service.create_user(db, user)
    
    return get_user_dict(db_user)

@router.get("/")
async def get_list(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    users = user_service.fetch_users(db);
    return [get_user_dict(u) for u in users]

@router.get("/{user_id}")
async def get_user(user_id: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    user = user_service.fetch_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    return get_user_dict(user)
