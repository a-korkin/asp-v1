from uuid import UUID
from db import db
from .models import User

def create_user(user: User):
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)
    return user

def fetch_all_users(offset: int = 0, limit: int = 10):
    return db.session.query(User).offset(offset).limit(limit).all()

def fetch_user(user_id: UUID):
    return db.session.query(User).filter_by(id=user_id).first()

def fetch_user_by_name(username: str):
    return db.session.query(User).filter_by(username=username).first()

def delete_user(user_id: UUID) -> bool:
    user = fetch_user(user_id)    
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    
    return False