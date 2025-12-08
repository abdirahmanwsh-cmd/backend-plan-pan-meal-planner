import logging
from fastapi import Response

logger = logging.getLogger(__name__)

try:
    # Import the main app (keeps existing application structure)
    from app.main import app
except Exception as e:
    # Log the error and fail loudly so we can see startup issues in logs
    logger.error(f"Failed to import app.main: {e}", exc_info=True)
    raise


# Ensure favicon requests return a simple 204 (avoids 500s when browsers request it)
@app.get("/favicon.ico", include_in_schema=False)
def favicon() -> Response:
    return Response(status_code=204)
