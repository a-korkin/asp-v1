from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_URL: str
    JWT_ACCESS_TOKEN_SECRET_KEY: str
    JWT_REFRESH_TOKEN_SECRET_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()        
