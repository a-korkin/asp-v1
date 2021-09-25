import os

class Config(object):
    DEBUG = True
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_SECRET_KEY = os.environ.get("JWT_ACCESS_TOKEN_SECRET_KEY")
    JWT_REFRESH_TOKEN_SECRET_KEY = os.environ.get("JWT_REFRESH_TOKEN_SECRET_KEY")

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
