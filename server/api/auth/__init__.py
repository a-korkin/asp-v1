import json
import os
import datetime
from flask import Blueprint, jsonify, request
from jose import jwt
from .models import User
from .schemas import user_schema, users_schema
from .crud import *
from functools import wraps

auth = Blueprint("auth", __name__, url_prefix="/auth")

def convert_input_to(class_):
    def wrap(f):
        def decorator(*args):
            obj = class_(**request.get_json())
            return f(obj)
        return decorator
    return wrap

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        
        if not token:
            return jsonify({"message": "token is missing!"}), 401
        
        try:
            secret_key = os.environ.get("SECRET_KEY")
            data = jwt.decode(token, secret_key)
            current_user = crud.fetch_user(data["user_id"])
        except:
            return jsonify({"message": "token is invalid!"}), 401

        return f(current_user, *args, **kwargs)            
    return decorated

@auth.route("/", methods=["GET"])
@login_required
def index(current_user: User):
    return jsonify({"message": current_user.username})

@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    pwd = data["password"]

    user = crud.fetch_user_by_name(username=username)
    if user:
        if user.verify_password(pwd):
            secret_key = os.environ.get("SECRET_KEY")
            token = jwt.encode({"user_id": str(user.id), "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=2), "iat": datetime.datetime.utcnow()}, secret_key, algorithm='HS256')
            return jsonify({"message": "success", "token": token})
        else:
            return jsonify({"message": "wrong password"})

    return jsonify({"message": "login"})

@auth.route("/users", methods=["POST"])    
@convert_input_to(User)
def create_user(user: User):
    print(user.username)
    print(user.password)

    data = request.get_json()
    u = user_schema.dump(data)
    try:
        db_user = crud.create_user(user)
        print(db_user.id)
    except Exception as e:
        print(e)

    return jsonify(u)

@auth.route("/users", methods=["GET"])    
def get_all():
    users = crud.fetch_all_users()
    return jsonify(users_schema.dump(users))

@auth.route("/users/<user_id>", methods=["GET"])    
def get_user(user_id):
    user = crud.fetch_user(user_id)
    if user:
        return jsonify(user_schema.dump(user))

    return jsonify({"message": "user not found"}), 404

@auth.route("/users/<user_id>", methods=["DELETE"])
def drop_user(user_id):
    result = crud.delete_user(user_id)
    
    if result:
        return jsonify({"message": "user deleted"})

    return jsonify({"message": "user not found"}), 404

