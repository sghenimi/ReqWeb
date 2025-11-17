from fastapi import FastAPI
from books_app.core.config import APP_NAME, APP_VERSION, APP_DEBUG
from books_app.core.logger import logger
from books_app.core.middleware import setup_middleware
from books_app.routers import books, health

def create_app() -> FastAPI:
    app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=APP_DEBUG)

    setup_middleware(app)

    app.include_router(health.router)
    app.include_router(books.router)

    logger.info(f"{APP_NAME} v{APP_VERSION} started")

    return app

