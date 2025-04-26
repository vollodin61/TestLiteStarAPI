from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.models.base import BaseModel


class User(BaseModel):
    """User model."""

    __tablename__ = "user"

    name: Mapped[str] = mapped_column(String(100))
    surname: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"<User {self.name} {self.surname}>"