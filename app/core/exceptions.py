from typing import Any, Dict

from litestar.exceptions import HTTPException


class NotFoundError(HTTPException):
    """Resource not found exception."""

    status_code = 404


class BadRequestError(HTTPException):
    """Bad request exception."""

    status_code = 400


class UnauthorizedError(HTTPException):
    """Unauthorized exception."""

    status_code = 401


class ForbiddenError(HTTPException):
    """Forbidden exception."""

    status_code = 403


class ConflictError(HTTPException):
    """Conflict exception."""

    status_code = 409