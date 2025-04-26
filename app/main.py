import logging

from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.di import Provide
from litestar.exceptions.http_exceptions import NotFoundException
from litestar.static_files.config import StaticFilesConfig

from app.api.routes import health_check
from app.api.user import UserController
from app.config import settings
from app.core.dependencies import exception_handler, not_found_handler
from app.domain.models.base import BaseModel
from app.infrastructure.database.session import get_db_session

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def create_db_tables() -> None:
    """Create database tables on startup."""
    from sqlalchemy.ext.asyncio import create_async_engine

    engine = create_async_engine(settings.DATABASE_URL)
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    await engine.dispose()


def create_app() -> Litestar:
    """Create and configure the Litestar application."""

    # Configure CORS
    cors_config = CORSConfig(
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    static_config = StaticFilesConfig(
        path="app/static",
        name="static",
        directories=["images", "css", "js"],
    )

    api_app = Litestar(
        route_handlers=[health_check, UserController],
        cors_config=cors_config,
        dependencies={"db_session": Provide(get_db_session)},  # Регистрируем зависимость для сессии БД
        exception_handlers={
            Exception: exception_handler,
            NotFoundException: not_found_handler,  # Специальный обработчик для 404
        },
        debug=settings.DEBUG,
        on_startup=[create_db_tables],
        static_files_config=[static_config],
    )

    return api_app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.UVICORN_RELOAD,
    )
