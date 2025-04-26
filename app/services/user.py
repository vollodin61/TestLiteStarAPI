from typing import List, Optional

from app.domain.models.user import User
from app.infrastructure.database.uow import UnitOfWork


class UserService:
    """User service for business logic."""

    @staticmethod
    async def create_user(uow: UnitOfWork, user_data: dict) -> User:
        """Create a new user."""
        async with uow:
            user = await uow.user_repository.create(user_data)
            await uow.commit()
            return user

    @staticmethod
    async def get_user(uow: UnitOfWork, user_id: int) -> Optional[User]:
        """Get a user by ID."""
        async with uow:
            return await uow.user_repository.get(user_id)

    @staticmethod
    async def get_all_users(uow: UnitOfWork) -> List[User]:
        """Get all users."""
        async with uow:
            return await uow.user_repository.get_all()

    @staticmethod
    async def update_user(uow: UnitOfWork, user_id: int, user_data: dict) -> Optional[User]:
        """Update a user."""
        async with uow:
            user = await uow.user_repository.update(user_id, user_data)
            await uow.commit()
            return user

    @staticmethod
    async def delete_user(uow: UnitOfWork, user_id: int) -> bool:
        """Delete a user."""
        async with uow:
            result = await uow.user_repository.delete(user_id)
            await uow.commit()
            return result