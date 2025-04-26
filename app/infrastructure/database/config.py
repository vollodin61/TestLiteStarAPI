from typing import AsyncGenerator

from advanced_alchemy.config import AsyncSessionConfig, SQLAlchemyAsyncConfig
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config import settings


class DatabaseConfig:
    """Database configuration."""

    def __init__(self, database_url: str):
        self.database_url = database_url
        self.engine = create_async_engine(
            database_url,
            echo=settings.DB_ECHO,
            pool_pre_ping=True,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Get a database session."""
        async with self.session_factory() as session:
            yield session


db_config = DatabaseConfig(settings.DATABASE_URL)

sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings.DATABASE_URL,
    session_config=AsyncSessionConfig(
        expire_on_commit=False,
    ),
    create_all=False,  # Мы создаем таблицы вручную в create_db_tables
)
