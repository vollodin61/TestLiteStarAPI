from abc import ABC, abstractmethod
from typing import Generic, List, Optional, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar('T')


class AbstractRepository(Generic[T], ABC):
    """Abstract repository interface."""

    @abstractmethod
    async def create(self, obj_in: dict) -> T:
        """Create a new object."""
        pass

    @abstractmethod
    async def get(self, id: int) -> Optional[T]:
        """Get an object by ID."""
        pass

    @abstractmethod
    async def get_all(self) -> List[T]:
        """Get all objects."""
        pass

    @abstractmethod
    async def update(self, id: int, obj_in: dict) -> Optional[T]:
        """Update an object."""
        pass

    @abstractmethod
    async def delete(self, id: int) -> bool:
        """Delete an object."""
        pass


class AbstractUserRepository(AbstractRepository[T], ABC):
    """Abstract user repository interface."""

    @abstractmethod
    async def get_by_name(self, name: str) -> Optional[T]:
        """Get a user by name."""
        pass