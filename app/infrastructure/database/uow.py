from abc import ABC, abstractmethod
from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.interfaces.repositories import AbstractRepository
from app.infrastructure.repositories.user import UserRepository


class AbstractUnitOfWork(ABC):
    """Abstract Unit of Work interface."""

    @abstractmethod
    async def __aenter__(self):
        """Enter the context manager."""
        pass

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit the context manager."""
        pass

    @abstractmethod
    async def commit(self):
        """Commit the transaction."""
        pass

    @abstractmethod
    async def rollback(self):
        """Rollback the transaction."""
        pass


class UnitOfWork(AbstractUnitOfWork):
    """Unit of Work implementation."""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.user_repository = UserRepository(session)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()

    async def commit(self):
        """Commit the transaction."""
        await self.session.commit()

    async def rollback(self):
        """Rollback the transaction."""
        await self.session.rollback()