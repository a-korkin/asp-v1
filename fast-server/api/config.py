from pydantic import BaseSettings

class Settings(BaseSettings):
    db_url: str
    jwt_access_token_secret_key: str
    jwt_refresh_token_secret_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()        
