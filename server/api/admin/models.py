from db import db, Entity, uuid, UUID
from werkzeug.security import generate_password_hash, check_password_hash

class User(Entity):
    __tablename__ = "cd_users"
    __table_args__ = {"schema": "admin", "comment": "пользователи"}
    id = db.Column(UUID(as_uuid=True), db.ForeignKey("common.cd_entities.id"), primary_key=True, default=uuid.uuid4, comment="идентификатор")
    username = db.Column("c_username", db.String(500), nullable=False, unique=True, index=True, comment="логин")
    password = db.Column("c_password", db.String(500), nullable=False, comment="пароль")
    lastname = db.Column("c_lastname", db.String(500), nullable=False, comment="фамилия")
    firstname = db.Column("c_firstname", db.String(500), nullable=False, comment="имя")
    middlename = db.Column("c_middlename", db.String(500), comment="отчество")

    __mapper_args__ = {
        "polymorphic_identity": "cd_users"
    }

    def __init__(self, username, password, lastname, firstname, middlename=None):
        self.username = username
        self.lastname = lastname
        self.firstname = firstname
        self.middlename = middlename
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f"<User {self.username}>"

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)        
