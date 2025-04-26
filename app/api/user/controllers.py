from typing import List

from litestar import Controller, get, post, put, delete, status_codes
from litestar.di import Provide
from litestar.exceptions import NotFoundException

from app.infrastructure.database.dependencies import provide_unit_of_work, UOWDependency
from app.api.user.schemas import UserCreate, UserResponse, UserUpdate
from app.services.user import UserService


class UserController(Controller):
    """User controller for handling user-related requests."""

    path = "/users"
    tags = ["users"]
    dependencies = {"uow": Provide(provide_unit_of_work)}

    @post("/", status_code=status_codes.HTTP_201_CREATED)
    async def create_user(self, data: UserCreate, uow: UOWDependency) -> UserResponse:
        """
        Create a new user.
        
        Args:
            data: User creation data
            uow: Unit of Work for database transactions
        
        Returns:
            Created user details
        """
        user = await UserService.create_user(uow, data.model_dump())
        return UserResponse(
            id=user.id,
            name=user.name,
            surname=user.surname,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    @get("/", status_code=status_codes.HTTP_200_OK)
    async def get_all_users(self, uow: UOWDependency) -> List[UserResponse]:
        """
        Get all users.
        
        Args:
            uow: Unit of Work for database transactions
        
        Returns:
            List of users
        """
        users = await UserService.get_all_users(uow)
        return [
            UserResponse(
                id=user.id,
                name=user.name,
                surname=user.surname,
                created_at=user.created_at,
                updated_at=user.updated_at,
            )
            for user in users
        ]

    @get("/{user_id:int}", status_code=status_codes.HTTP_200_OK)
    async def get_user(self, user_id: int, uow: UOWDependency) -> UserResponse:
        """
        Get a user by ID.
        
        Args:
            user_id: Unique identifier of the user
            uow: Unit of Work for database transactions
        
        Returns:
            User details
        
        Raises:
            NotFoundException: If user is not found
        """
        user = await UserService.get_user(uow, user_id)
        if not user:
            raise NotFoundException(f"User with ID {user_id} not found")
        return UserResponse(
            id=user.id,
            name=user.name,
            surname=user.surname,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    @put("/{user_id:int}", status_code=status_codes.HTTP_200_OK)
    async def update_user(self, user_id: int, data: UserUpdate, uow: UOWDependency) -> UserResponse:
        """
        Update a user.
        
        Args:
            user_id: Unique identifier of the user
            data: User update data
            uow: Unit of Work for database transactions
        
        Returns:
            Updated user details
        
        Raises:
            NotFoundException: If user is not found
        """
        # Filter out None values
        update_data = {k: v for k, v in data.model_dump().items() if v is not None}
        user = await UserService.update_user(uow, user_id, update_data)
        if not user:
            raise NotFoundException(f"User with ID {user_id} not found")
        return UserResponse(
            id=user.id,
            name=user.name,
            surname=user.surname,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    @delete("/{user_id:int}", status_code=status_codes.HTTP_204_NO_CONTENT)
    async def delete_user(self, user_id: int, uow: UOWDependency) -> None:
        """
        Delete a user.
        
        Args:
            user_id: Unique identifier of the user
            uow: Unit of Work for database transactions
        
        Raises:
            NotFoundException: If user is not found
        """
        result = await UserService.delete_user(uow, user_id)
        if not result:
            raise NotFoundException(f"User with ID {user_id} not found")
