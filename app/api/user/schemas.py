from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class UserBase(BaseModel):
    """Base user schema."""

    name: str = Field(..., min_length=2, max_length=50)
    surname: str = Field(..., min_length=2, max_length=50)

    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    """User creation schema."""

    password: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    """User update schema."""

    name: Optional[str] = Field(None, min_length=2, max_length=50)
    surname: Optional[str] = Field(None, min_length=2, max_length=50)
    password: Optional[str] = Field(None, min_length=8)

    model_config = ConfigDict(from_attributes=True)


class UserResponse(UserBase):
    """User response schema."""

    id: int
    created_at: datetime
    updated_at: datetime