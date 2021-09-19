import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from db import Entity

# class Entity(Base):
#     __tablename__ = "cd_entities"
#     __table_args__ = {"schema": "public", "comment": "сущности"}
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, comment="идентификатор")

#     __mapper_args__ = {
#         'polymorphic_identity':'cd_entities'
#     }

class User(Entity):
    __tablename__ = 'cd_users'
    __table_args__ = {"schema": "auth", "comment": "пользователи"}
    id = Column(UUID(as_uuid=True), ForeignKey('common.cd_entities.id'), primary_key=True, default=uuid.uuid4, comment="идетификатор")
    username = Column("c_username", String(500), unique=True, nullable=False, index=True, comment="имя пользователя")
    password = Column("c_password", String(500), nullable=False, comment="пароль")
    lastname = Column("c_lastname", String(500), nullable=False, comment="фамилия")
    firstname = Column("c_firstname", String(500), nullable=False, comment="имя")
    middlename = Column("c_middlename", String(500), comment="отчество")

    __mapper_args__ = {
        'polymorphic_identity':'cd_users',
    }
