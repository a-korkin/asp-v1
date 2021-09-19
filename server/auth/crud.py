from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.User):
    db_user = models.User(username=user.username, password=user.password, lastname=user.lastname, firstname=user.firstname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user