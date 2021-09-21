from functools import wraps
from flask import request, jsonify, current_app
from jose import jwt
from api.admin.crud import fetch_user

def token_required(f):
    """декоратор для проверки токена"""
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        X_ACCESS_TOKEN = "x-access-token"

        if X_ACCESS_TOKEN in request.headers:
            token = request.headers[X_ACCESS_TOKEN]

        if not token:
            return jsonify({"message": "token is missing"}), 401

        try:
            SECRET_KEY = current_app.config["SECRET_KEY"] #os.environ.get("SECRET_KEY")
            data = jwt.decode(token, SECRET_KEY)
            current_user = fetch_user(data["user_id"])
        except:
            return jsonify({"message": "token is invalid"}), 401

        return f(current_user, *args, *kwargs)

    return decorator

def convert_input_to(class_):
    """декоратор для десериализации в объект запроса"""
    def wrap(f):
        def decorator(*args, **kwargs):
            obj = class_(**request.get_json())
            return f(obj)
        return decorator
    return wrap
