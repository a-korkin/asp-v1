import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()

class Entity(db.Model):
    __tablename__ = "cd_entities"
    __table_args__ = {"schema": "common", "comment": "сущности"}
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, comment="идентификатор")

    __mapper_args__ = {
        "polymorphic_identity": "cd_entities"
    }
