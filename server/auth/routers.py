from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from db.database import SessionLocal
from . import crud, schemas

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_user", response_model=schemas.User)
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return db_user
