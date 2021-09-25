from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from api.db import Base, Column, String, UUID, uuid

class User(Base):
    __tablename__ = "cd_users"
    __table_args__ = {"schema": "auth", "comment": "пользователи"}
    id = Column(UUID(as_uuid=True), ForeignKey("common.cd_entities.id"), primary_key=True, default=uuid.uuid4)
    username = Column(String(500), unique=True, nullable=False, index=True)
