from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from books_app.core.logger import logger
import time

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        logger.info(f"Request: {request.method} {request.url}")

        response: Response = await call_next(request)

        process_time = (time.time() - start_time) * 1000
        logger.info(f"Response: status_code={response.status_code} completed_in={process_time:.2f}ms")
        return response

def setup_middleware(app):
    # Keep existing middleware here if any (e.g. CORS)
    from fastapi.middleware.cors import CORSMiddleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(LoggingMiddleware)
