from db import ma
from .models import User

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        fields = ("username", "password")

