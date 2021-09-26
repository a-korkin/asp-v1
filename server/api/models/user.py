# import uuid
from api.db import Entity, Column, String, UUID, uuid
from sqlalchemy.sql.schema import ForeignKey

class User(Entity):
    __tablename__ = "cd_users"
    __table_args__ = {"schema": "auth", "comment": "пользователи"}
    id = Column(UUID(as_uuid=True), ForeignKey("common.cd_entities.id"), primary_key=True, default=uuid.uuid4)
    username = Column("c_username", String(500), unique=True, nullable=False, index=True)
    password = Column("c_password", String(500), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"        
