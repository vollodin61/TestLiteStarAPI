from typing import Annotated

from litestar.di import Provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.uow import UnitOfWork


async def provide_unit_of_work(db_session: AsyncSession) -> UnitOfWork:
    """Provide a Unit of Work instance."""
    return UnitOfWork(db_session)


# Dependency providers
UOWDependency = Annotated[UnitOfWork, Provide(provide_unit_of_work)]