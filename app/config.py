import os
from typing import Any, Dict

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """Application settings."""

    # Application settings
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    DB_ECHO: bool = os.getenv("DB_ECHO", "False").lower() in ("true", "1", "t")
    UVICORN_RELOAD: bool = os.getenv("UVICORN_RELOAD", "False").lower() in ()
    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/user_db")

    # API settings
    API_PREFIX: str = "/api"
    API_VERSION: str = "v1"
    OPENAPI_URL: str = "/openapi.json"
    DOCS_URL: str = "/docs"

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        """Return kwargs for FastAPI initialization."""
        return {
            "debug": self.DEBUG,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
        }


settings = Settings()
