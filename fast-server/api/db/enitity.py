import uuid
from .database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

class Entity(Base):
    __tablename__ = "cd_entities"
    __table_args__ = {"schema": "common", "comment": "сущности"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, comment="идентификатор")
