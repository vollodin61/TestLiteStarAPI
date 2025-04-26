from datetime import datetime

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import BigInteger, func
from sqlalchemy.orm import Mapped, mapped_column


class TimestampMixin:
    """Mixin for timestamp fields."""

    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        onupdate=func.now(),
        server_default=func.now(),
    )


class BaseModel(BigIntAuditBase, TimestampMixin):
    """Base model for all models."""

    __abstract__ = True

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
