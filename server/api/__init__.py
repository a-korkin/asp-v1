from flask import Flask 
from flask_migrate import Migrate
# from flask_marshmallow import Marshmallow
from .auth import auth as auth_blueprint, models
from db import db, ma
from config import config

# ma = Marshmallow()

def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app=app)
    Migrate(app=app, db=db)
    ma.init_app(app=app)

    # blueprints
    app.register_blueprint(auth_blueprint)
    

    return app
