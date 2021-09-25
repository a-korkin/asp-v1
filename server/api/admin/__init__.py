import datetime
from api.utils import token_required, convert_input_to
from flask import Blueprint, jsonify, request, current_app, make_response
from jose import jwt
from .models import User
from .schemas import user_schema, users_schema
from .crud import *

admin = Blueprint("admin", __name__)

def refresh_tokens(user: User):
    """обновление токена"""   
    JWT_ACCESS_TOKEN_SECRET_KEY = current_app.config["JWT_ACCESS_TOKEN_SECRET_KEY"]
    JWT_REFRESH_TOKEN_SECRET_KEY = current_app.config["JWT_REFRESH_TOKEN_SECRET_KEY"]
    user_dict_access = {
        "user_id": str(user.id), 
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15), 
        "iat": datetime.datetime.utcnow()
    }

    user_dict_refresh = {
        "user_id": str(user.id), 
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=2), 
        "iat": datetime.datetime.utcnow()
    }

    access_token = jwt.encode(user_dict_access, JWT_ACCESS_TOKEN_SECRET_KEY, algorithm='HS256')
    refresh_token = jwt.encode(user_dict_refresh, JWT_REFRESH_TOKEN_SECRET_KEY, algorithm='HS256')
    resp = make_response(jsonify({"accessToken": f"Bearer {access_token}"}))
    resp.set_cookie("refreshToken", value=refresh_token, httponly=True)
    crud.update_user(user, refresh_token)
    return resp

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
            resp = refresh_tokens(user)
            return resp, 200
        else:
            return jsonify({"message": "wrong password"}), 403

    return jsonify({"message": "wrong login or password"}), 403

@admin.route("/logout", methods=["POST"]) 
@token_required   
def logout(current_user: User): 
    crud.update_user(current_user, None)
    return jsonify({"message": f"{current_user.username} is logged out"}), 200

@admin.route("/refresh", methods=["POST"])    
@token_required
def refresh(current_user: User):
    resp = refresh_tokens(current_user)
    return resp, 200

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
