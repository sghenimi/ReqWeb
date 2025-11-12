import unicodedata

import uvicorn
from fastapi import FastAPI, HTTPException, Query, Request
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID
from loguru import logger
from starlette.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Charger les variables d'environnement
load_dotenv()

# ----- Config -----
APP_NAME = os.getenv("APP_NAME", "Book API")
APP_DEBUG = os.getenv("APP_DEBUG", "False") == "True"
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
SERVER_HOST = os.getenv("SERVER_HOST", "127.0.0.1")
SERVER_PORT = int(os.getenv("SERVER_PORT", 8000))
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./books.db")

# ----- Rate limiter -----
limiter = Limiter(key_func=get_remote_address)
# Initialisation de FastAPI
app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    debug=APP_DEBUG
)

# Register rate limit handler
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# ----- Data Models -----
class Book(BaseModel):
    id: UUID
    title: str
    author: str
    year: Optional[int] = None
    description: Optional[str] = None


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    description: Optional[str] = None


# ----- In-memory database -----
books_db: List[Book] = [
    Book(id=uuid4(), title="Le Petit Prince", author="Antoine de Saint-Exupéry", year=1943,
         description="Un conte poétique sur l'amitié et la vie."),
    Book(id=uuid4(), title="L'Étranger", author="Albert Camus", year=1942,
         description="Un roman existentiel sur l'absurdité de la condition humaine."),
    Book(id=uuid4(), title="1984", author="George Orwell", year=1949,
         description="Une dystopie sur la surveillance et le totalitarisme."),
    Book(id=uuid4(), title="Harry Potter à l'école des sorciers", author="J.K. Rowling", year=1997,
         description="Le premier tome de la célèbre série magique."),
    Book(id=uuid4(), title="Les Misérables", author="Victor Hugo", year=1862,
         description="Une épopée humaine et sociale dans la France du XIXe siècle.")
]


# ----- Helper pour normaliser les chaînes -----
def normalize(text: str) -> str:
    normalized = unicodedata.normalize('NFD', text)
    return ''.join(c for c in normalized if unicodedata.category(c) != 'Mn').lower()


# ----- Health check -----
@app.get("/health")
@limiter.limit("5/minute")
def health_check(request: Request):
    return {"status": "ok", "message": "API is healthy"}


# ----- Pagination -----
@app.get("/books/", response_model=List[Book])
def get_books(request: Request,
        page: int = Query(1, ge=1, description="Page number (starting at 1)"),
        limit: int = Query(10, ge=1, le=50, description="Number of books per page")
):
    start = (page - 1) * limit
    end = start + limit
    return books_db[start:end]


# ----- Recherche partielle sans accents -----
@app.get("/books/search/{title}", response_model=List[Book])
def search_books(title: str):
    normalized_query = normalize(title)
    results = [
        book for book in books_db
        if normalized_query in normalize(book.title)
    ]
    if not results:
        raise HTTPException(status_code=404, detail="No books found matching title")
    return results


# ----- Create -----
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    for b in books_db:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    books_db.append(book)
    return book


@app.post("/books/auto", response_model=Book)
def create_book_auto(book: Book):
    new_book = Book(id=uuid4(), **book.dict())
    books_db.append(new_book)
    return new_book


# ----- Update -----
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: UUID, data: BookUpdate):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            updated_data = data.dict(exclude_unset=True)
            updated_book = book.copy(update=updated_data)
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


# ----- Delete -----
@app.delete("/books/{book_id}")
def delete_book(book_id: UUID):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            del books_db[index]
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")


app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])
if __name__ == "__main__":
    logger.info("Starting app...")
    uvicorn.run("main:app",
                host=SERVER_HOST,
                port=SERVER_PORT,
                reload=True,
                log_level="debug",
                # workers=1,
                # limit_concurrency=1,
                # limit_max_requests=1
                )
