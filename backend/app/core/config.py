import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / ".env"

class Settings(BaseSettings):
    APP_NAME: str = "SMRITHI Backend API"
    APP_VERSION: str = "1.0.0"
    APP_ENV: str = "development"
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Security
    SECRET_KEY: str = "smrithi-secret-key-change-this-in-production-ner-sih26003"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24 hours
    
    # Database
    MONGODB_URI: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "smrithi_db"
    USE_IN_MEMORY_FALLBACK: bool = True
    
    # External AI / LLM APIs
    GEMINI_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    
    # Storage
    AUDIO_CACHE_DIR: str = str(BASE_DIR / "audio_cache")

    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE) if ENV_FILE.exists() else None,
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()