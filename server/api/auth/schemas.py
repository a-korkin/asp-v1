from marshmallow_sqlalchemy.schema import SQLAlchemySchema
from .models import User

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        fields = ("username", "password")

user_schema = UserSchema()
users_schema = UserSchema(many=True)
