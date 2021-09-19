import os
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    db_url: str
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
