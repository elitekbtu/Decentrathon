# backend/app/config.py

import os
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    DATABASE_URL: str = Field(..., env='DATABASE_URL')
    SECRET_KEY: str = Field(..., env='SECRET_KEY')
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 день
    OPENAI_API_KEY: str = Field(..., env='OPENAI_API_KEY')

    class Config:
        env_file = "../shared/config/.env"

settings = Settings()
