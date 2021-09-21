from flask import Flask 
from flask_migrate import Migrate
from .admin import admin as admin_blueprint
from db import db
from .config import config

def create_app(config_name="default"):
    """создание приложения"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app=app)
    Migrate(app=app, db=db)

    # blueprints
    app.register_blueprint(admin_blueprint)
    
    return app
