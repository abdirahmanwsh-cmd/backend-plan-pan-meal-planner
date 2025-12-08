from fastapi import Response

try:
    # Import the main app (keeps existing application structure)
    from app.main import app
except Exception:
    # If importing app.main fails for some reason, create a minimal fallback
    from fastapi import FastAPI
    app = FastAPI(title="FitPlate API (fallback)")


# Ensure favicon requests return a simple 204 (avoids 500s when browsers request it)
@app.get("/favicon.ico", include_in_schema=False)
def favicon() -> Response:
    return Response(status_code=204)
