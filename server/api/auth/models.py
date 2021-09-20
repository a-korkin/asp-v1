from db import db, Entity, uuid, UUID

class User(Entity):
    __tablename__ = "cd_users"
    __table_args__ = {"schema": "admin", "comment": "пользователи"}
    id = db.Column(UUID(as_uuid=True), db.ForeignKey("common.cd_entities.id"), primary_key=True, default=uuid.uuid4, comment="идентификатор")
    username = db.Column("c_username", db.String(500), nullable=False, unique=True, index=True, comment="логин")
    password = db.Column("c_password", db.String(500), nullable=False, comment="пароль")


    # def to_json(self):
    #     return json.dumps(self, default=lambda o: o._asdict(), sort_keys=True, indent=4)

    # def as_dict(self):
    #    return {c.name: getattr(self, c.name) for c in self.__table__.attr}        

    __mapper_args__ = {
        "polymorphic_identity": "cd_users"
    }

    # def to_json(self):
    #     self.__dict__
        # return json.dumps(self.__dict__)
