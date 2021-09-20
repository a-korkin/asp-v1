from flask import Blueprint, jsonify, request
from .models import User
from .schemas import UserSchema

auth = Blueprint("auth", __name__, url_prefix="/auth")

def convert_input_to(class_):
    def wrap(f):
        def decorator(*args):
            obj = class_(**request.get_json())
            return f(obj)
        return decorator
    return wrap

@auth.route("/", methods=["GET"])
def index():
    return jsonify({"message": "test"})

@auth.route("/users", methods=["POST"])    
@convert_input_to(User)
def create_user(user: User):
    user_schema = UserSchema()
    u = user_schema.dump(user)
    return jsonify(u)
