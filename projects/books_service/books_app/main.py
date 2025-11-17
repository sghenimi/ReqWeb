import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from books_app.config import APP_NAME, APP_VERSION, APP_DEBUG, SERVER_HOST, SERVER_PORT
from books_app.database_books import Base, engine
from books_app.routers import books, health

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    debug=APP_DEBUG
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(books.router)
app.include_router(health.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVER_HOST, port=SERVER_PORT, reload=True)

