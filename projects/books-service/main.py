import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str
    author: str
    description: Optional[str] = None

# modèle utilisé pour les requêtes PUT/PATCH
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None


# In-memory storage
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


# ----- Health check -----
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is healthy"}


@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    book.id = uuid4()
    for b in books_db:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    books_db.append(book)
    return book


@app.get("/books/", response_model=List[Book])
async def read_books():
    return books_db


@app.get("/books/{title}", response_model=List[Book])
async def get_book(title: str):
    _found_books = [_book for _book in books_db if title.lower() in _book.title.lower()]
    if not _found_books:
        raise HTTPException(status_code=404, detail="Book not found")
    return _found_books


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: UUID, data: BookUpdate):
    for _index, _book in enumerate(books_db):
        if _book.id == book_id:
            updated_data = data.model_dump(exclude_unset=True)  # ne modifie que les champs envoyés
            updated_book = _book.model_copy(update=updated_data)
            books_db[_index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", response_model=Book)
async def delete_book(book_id: UUID):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            return books_db.pop(index)
    raise HTTPException(status_code=404, detail="Book not found")

# app.add_middleware(CORSMiddleware,
#                    allow_origins=["*"],
#                    allow_methods=["*"],
#                    allow_headers=["*"])
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="localhost", port=8000,
#                 reload=True, log_level="debug",
#                 workers=1, limit_concurrency=1, limit_max_requests=1)
