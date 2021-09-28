from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from api.crud import user as crud_user
from typing import Optional
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose.constants import ALGORITHMS
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from api.config import settings
from api.db import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(pwd: str, hash: str):
    return pwd_context.verify(pwd, hash)

def get_password_hash(pwd: str):
    return pwd_context.hash(pwd)   

def create_token(data: dict, secret_key: str, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)    
    
    to_encode.update({"exp": expire, "iat": datetime.utcnow()})

    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=ALGORITHMS.HS256)
    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")    

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):   
    credential_exception = HTTPException(status_code=401, detail="could not validate credentials")
    secret_key = settings.JWT_ACCESS_TOKEN_SECRET_KEY
    username: str
    try:
        payload = jwt.decode(token=token, key=secret_key, algorithms=ALGORITHMS.HS256)
        username = payload["user"]
        if username is None:
            raise credential_exception
    except JWTError:
        raise credential_exception
    
    user = crud_user.fetch_user_by_name(db=db, username=username)
    if user is None:
        raise credential_exception
    
    return user

def check_refresh_token(token: str, db: Session):
    try:
        credential_exception = HTTPException(status_code=401, detail="could not validate credentials")
        secret_key = settings.JWT_REFRESH_TOKEN_SECRET_KEY
        payload = jwt.decode(token=token, key=secret_key, algorithms=ALGORITHMS.HS256)
        username = payload["user"]

        if username is None:
            raise credential_exception
        
        user = crud_user.fetch_user_by_name(db=db, username=username)
        return user

    except JWTError:
        raise credential_exception
