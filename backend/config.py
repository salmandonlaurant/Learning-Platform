import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "CyberSec Tutor"
    DATABASE_URL: str = "sqlite+aiosqlite:///./cybersec_tutor.db"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    class Config:
        env_file = ".env"


settings = Settings()
