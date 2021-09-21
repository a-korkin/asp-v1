import datetime
from api.utils import token_required, convert_input_to
from flask import Blueprint, jsonify, request, current_app
from jose import jwt
from .models import User
from .schemas import user_schema, users_schema
from .crud import *

admin = Blueprint("admin", __name__)

@admin.route("/", methods=["GET"])
def index():
    print(request.headers["Authorization"])
    return jsonify({"message": "index"})

@admin.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    pwd = data["password"]

    user = crud.fetch_user_by_name(username=username)
    if user:
        if user.verify_password(pwd):
            secret_key = current_app.config["SECRET_KEY"]
            user_dict = {
                "user_id": str(user.id), 
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15), 
                "iat": datetime.datetime.utcnow()
            }

            token = jwt.encode(user_dict, secret_key, algorithm='HS256')
            return jsonify({"message": "success", "accessToken": f"Bearer {token}"}), 200
        else:
            return jsonify({"message": "wrong password"}), 403

    return jsonify({"message": "wrong login or password"}), 403

@admin.route("/users", methods=["POST"]) 
@token_required
def create_user(current_user: User):
    data = request.get_json()
    user_sch = user_schema.dump(data)
    user = User(
        username=data["username"],
        password=data["password"],
        lastname=data["lastname"],
        firstname=data["firstname"]
    )
    try:
        db_user = crud.create_user(user)
        if not db_user:
            return jsonify({"message": "user already exists"}), 400
    except:
        return jsonify({"message": "bad request"}), 400

    return jsonify(user_sch), 201

@admin.route("/users", methods=["GET"])    
@token_required
def get_all_users(current_user: User):
    users = crud.fetch_all_users()
    if users:
        return jsonify(users_schema.dump(users)), 200
    
    return jsonify({"message": "users not found"}), 204

@admin.route("/users/<user_id>", methods=["GET"])    
@token_required
def get_user(current_user: User, user_id):
    user = crud.fetch_user(user_id)
    if user:
        return jsonify(user_schema.dump(user))

    return jsonify({"message": "user not found"}), 404

@admin.route("/users/<user_id>", methods=["DELETE"])
@token_required
def drop_user(current_user: User, user_id):
    user = crud.delete_user(user_id)
    
    if user:
        return jsonify({"message": "user deleted"})

    return jsonify({"message": "user not found"}), 404
