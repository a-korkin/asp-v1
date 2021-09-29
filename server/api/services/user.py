import uuid
from sqlalchemy.orm.session import Session
from api.models.user import User
from api.schemas.user import UserCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        password=user.password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def fetch_users(db: Session, offset: int = 0, limit: int = 10):
    return db.query(User).offset(offset).limit(limit).all()

def fetch_user(db: Session, user_id: uuid.UUID):
    return db.query(User).filter_by(id=user_id).first()

def fetch_user_by_name(db: Session, username: str) -> User:
    return db.query(User).filter_by(username=username).first()

def update_user(db: Session, user: User):    
    db.commit()
    db.refresh(user)
    return user

def drop_user(db: Session, user: User):
    db.delete(user)    
    db.commit()