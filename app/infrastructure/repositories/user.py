from typing import List, Optional, Type

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.interfaces.repositories import AbstractUserRepository
from app.domain.models.user import User


class UserRepository(AbstractUserRepository[User]):
    """User repository implementation."""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.model = User

    async def create(self, obj_in: dict) -> User:
        """Create a new user."""
        db_obj = self.model(**obj_in)
        self.session.add(db_obj)
        await self.session.flush()
        return db_obj

    async def get(self, id: int) -> Optional[User]:
        """Get a user by ID."""
        query = select(self.model).where(self.model.id == id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_all(self) -> List[User]:
        """Get all users."""
        query = select(self.model)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def update(self, id: int, obj_in: dict) -> Optional[User]:
        """Update a user."""
        query = (
            update(self.model)
            .where(self.model.id == id)
            .values(**obj_in)
            .returning(self.model)
        )
        result = await self.session.execute(query)
        await self.session.flush()
        return result.scalars().first()

    async def delete(self, id: int) -> bool:
        """Delete a user."""
        query = delete(self.model).where(self.model.id == id)
        result = await self.session.execute(query)
        return result.rowcount > 0

    async def get_by_name(self, name: str) -> Optional[User]:
        """Get a user by name."""
        query = select(self.model).where(self.model.name == name)
        result = await self.session.execute(query)
        return result.scalars().first()