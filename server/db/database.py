import uuid
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Settings

SQLALCHEMY_DATABASE_URL = Settings().db_url
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Entity(Base):
    __tablename__ = "cd_entities"
    __table_args__ = {"schema": "common", "comment": "сущности"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, comment="идентификатор")

    __mapper_args__ = {
        'polymorphic_identity':'cd_entities'
    }
