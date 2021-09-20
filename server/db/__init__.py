import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.inspection import inspect
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

uuid = uuid
UUID = UUID

class Entity(db.Model):
    __tablename__ = "cd_entities"
    __table_args__ = {"schema": "common", "comment": "сущности"}
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, comment="идентификатор")

    __mapper_args__ = {
        "polymorphic_identity": "cd_entities"
    }

# class Serializer(object):
#     def serialize(self):
#         return {c: getattr(self, c) for c in inspect(self).attr.keys()}

#     @staticmethod
#     def serialize_list(l):
#         return [m.serialize() for m in l]        
