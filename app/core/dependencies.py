import logging

from litestar import Request
from litestar.exceptions import HTTPException
from litestar.exceptions.http_exceptions import NotFoundException
from litestar.response import Response
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_404_NOT_FOUND

# Configure logging
logger = logging.getLogger(__name__)


def exception_handler(request: Request, exc: Exception) -> Response:
    """Handle HTTP exceptions."""
    logger.info(f"Handling exception: {exc}")
    if isinstance(exc, HTTPException):
        status_code = exc.status_code
        detail = exc.detail
    else:
        status_code = HTTP_500_INTERNAL_SERVER_ERROR
        detail = str(exc)

    response = Response(
        content={"status_code": status_code, "detail": detail},
        status_code=status_code,
    )
    logger.info(f"Returning response: {response}")
    return response


def not_found_handler(
        request: Request,
        exc: NotFoundException,
) -> Response:
    """Handle 404 Not Found exceptions specifically."""
    # logger.info(f"Handling 404 exception: {exc}")

    # Создаем более дружелюбный ответ для 404
    response = Response(
        content={
            "status_code": HTTP_404_NOT_FOUND,
            "detail": f"The requested resource '{request.url.path}' was not found"
        },
        status_code=HTTP_404_NOT_FOUND,
    )
    # logger.info(f"Returning 404 response: {response}")
    return response
