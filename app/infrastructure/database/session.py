from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.config import db_config


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Get a database session."""
    async with db_config.session_factory() as session:
        yield session
