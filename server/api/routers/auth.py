import traceback
from typing import Optional
from datetime import timedelta
from fastapi import APIRouter, HTTPException, Response
from fastapi.params import Cookie, Depends
from sqlalchemy.orm.session import Session
from api.config import settings
from api.models.user import User
from api.crud import user as crud_user
from api.schemas.auth import AuthInDTO, AuthOutDTO
from api.schemas.user import UserDTO
from api.utils import get_db, create_token, verify_password, get_password_hash, get_current_user, check_refresh_token

router = APIRouter()  

def get_tokens(user: User, response: Response, db: Session) -> AuthOutDTO:
    access_token = create_token({"user": user.username}, settings.JWT_ACCESS_TOKEN_SECRET_KEY, timedelta(minutes=15))
    refresh_token = create_token({"user": user.username}, settings.JWT_REFRESH_TOKEN_SECRET_KEY, timedelta(days=10))
          
    user.refresh_token = refresh_token
    crud_user.update_user(db, user)
    response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
    return AuthOutDTO(access_token=access_token, user=UserDTO(username=user.username))
   
@router.post("/login", response_model=AuthOutDTO)    
async def login(auth_in: AuthInDTO, response: Response, db: Session = Depends(get_db)):
    user: User = crud_user.fetch_user_by_name(db, auth_in.username)
    if not user:
        raise HTTPException(status_code=403, detail="access denied")
    
    if not verify_password(auth_in.password, user.password):
        raise HTTPException(status_code=403, detail="access denied")

    try:
        resp = get_tokens(user=user, response=response, db=db)
        return resp
    except:  
        raise HTTPException(status_code=403, detail="access denied")

@router.post("/logout")    
async def logout(response: Response, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    current_user.refresh_token = None
    crud_user.update_user(db=db, user=current_user)
    response.delete_cookie(key="refresh_token")
    return {"detail": "logged out"}

@router.get("/refresh", response_model=AuthOutDTO)    
async def refresh(response: Response, refresh_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):
    try:
        user = check_refresh_token(token=refresh_token, db=db)
        resp = get_tokens(user=user, response=response, db=db)
        return resp
    except:
        raise HTTPException(status_code=401, detail="unauthorized")




# @router.post("/users", status_code=201)
# async def create_user(user: UserSchema, db: Session = Depends(get_db)):
#     db_user = crud_user.fetch_user_by_name(db=db, username=user.username)
#     if db_user:
#         raise HTTPException(status_code=400, detail="user already exists")

#     user.password = get_password_hash(user.password)
#     db_user = crud_user.create_user(db, user)
#     return {"message": "user created"}

# @router.get("/users/{user_id}", status_code=200)    
# async def get_user(user_id: UUID, db: Session = Depends(get_db)):
#     db_user = crud_user.fetch_user(db, user_id)
#     if not db_user:
#         raise HTTPException(status_code=404, detail="user not found")
    
#     return db_user

# @router.delete("/users/{user_id}", status_code=204)
# async def delete_user(user_id: UUID, db: Session = Depends(get_db)):
#     db_user = crud_user.fetch_user(db, user_id)
#     if not db_user:
#         raise HTTPException(status_code=404, detail="user not found")
    
#     crud_user.drop_user(db=db, user=db_user)
#     return {"message": "user deleted"}
