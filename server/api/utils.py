from functools import wraps
from flask import request, jsonify, current_app
from jose import jwt
from api.admin.crud import fetch_user

def token_required(f):
    """декоратор для проверки токена"""
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        AUTHORIZATION = "Authorization"

        if AUTHORIZATION in request.headers:
            token = request.headers[AUTHORIZATION].replace("Bearer ", "")

        if not token:
            return jsonify({"message": "token is missing"}), 401

        try:
            JWT_ACCESS_TOKEN_SECRET_KEY = current_app.config["JWT_ACCESS_TOKEN_SECRET_KEY"]
            data = jwt.decode(token, JWT_ACCESS_TOKEN_SECRET_KEY)
            current_user = fetch_user(data["user_id"])
        except:
            return jsonify({"message": "token is invalid"}), 401

        return f(current_user, *args, *kwargs)

    return decorator

def convert_input_to(class_):
    """декоратор для десериализации в объект запроса"""
    def wrap(f):
        def decorator(*args, **kwargs):
            print(str(**request.get_json()))
            obj = class_(**request.get_json())
            return f(obj, *args, **kwargs)
        return decorator
    return wrap
