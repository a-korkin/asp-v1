import os
from re import DEBUG 

class Config(object):
    DEBUG = True
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")

class DevelopmentConfig(Config):
    pass

class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"

config = {
    "default": DevelopmentConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig
}    
