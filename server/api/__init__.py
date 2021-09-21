from flask import Flask 
from flask_migrate import Migrate
from .auth import auth as auth_blueprint
from db import db
from .config import config

# conf = config["default"]

def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app=app)
    Migrate(app=app, db=db)

    # blueprints
    app.register_blueprint(auth_blueprint)
    

    return app
