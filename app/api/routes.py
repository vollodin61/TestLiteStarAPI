from litestar import get


@get("/")
async def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "ok"}
