import json
from db import db, Entity, uuid, UUID

class User(Entity):
    __tablename__ = "cd_users"
    __table_args__ = {"schema": "admin", "comment": "пользователи"}
    id = db.Column(UUID(as_uuid=True), db.ForeignKey("common.cd_entities.id"), primary_key=True, default=uuid.uuid4, comment="идентификатор")
    username = db.Column("c_username", db.String(500), nullable=False, unique=True, index=True, comment="логин")
    password = db.Column("c_password", db.String(500), nullable=False, comment="пароль")

    __mapper_args__ = {
        "polymorphic_identity": "cd_users"
    }
    