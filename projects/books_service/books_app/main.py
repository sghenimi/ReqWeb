# import uvicorn
# from fastapi import FastAPI
# from starlette.middleware.cors import CORSMiddleware
#
# from books_app.core.config import APP_NAME, APP_VERSION, APP_DEBUG, SERVER_HOST, SERVER_PORT
# from books_app.core.logger import logger
# from books_app.core.logging_middleware import LoggingMiddleware
# from books_app.core.database_books import Base, engine
# from books_app.routers import books, health
# # Create DB tables
# Base.metadata.create_all(bind=engine)
#
# app = FastAPI(
#     title=APP_NAME,
#     version=APP_VERSION,
#     debug=APP_DEBUG
# )
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"]
# )
# app.add_middleware(LoggingMiddleware)
#
# app.include_router(books.router)
# app.include_router(health.router)
#
# if __name__ == "__main__":
#     logger.info("Starting FastAPI app...")
#     uvicorn.run("main:app", host=SERVER_HOST, port=SERVER_PORT, reload=True)
#
import uvicorn

from books_app.core.app import create_app
from books_app.core.config import SERVER_HOST, SERVER_PORT
from books_app.core.database_books import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVER_HOST, port=SERVER_PORT, reload=True)
