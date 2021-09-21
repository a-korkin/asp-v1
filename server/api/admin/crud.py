from uuid import UUID
from db import db
from .models import User

def create_user(user: User):
    """создание пользователя"""
    try:
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        return user
    except:
        return None

def fetch_all_users(offset: int = 0, limit: int = 10):
    """получение списка пользователей"""
    return db.session.query(User).offset(offset).limit(limit).all()

def fetch_user(user_id: UUID):
    """получение пользователя по идентификатору"""
    return db.session.query(User).filter_by(id=user_id).first()

def fetch_user_by_name(username: str):
    """получение пользователя по логину"""
    return db.session.query(User).filter_by(username=username).first()

def delete_user(user_id: UUID):
    """удаление пользователя"""
    user = fetch_user(user_id)    
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    
    return False