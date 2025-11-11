from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str
    author: str
    description: Optional[str] = None


# In-memory storage
books_db: List[Book] = []


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


@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_title: str):
    _found_books:List[Book] = []
    for _book in books_db:
        if book_title.lower() in _book.title.lower():
            _found_books.append(_book)

    if _found_books:
        return _found_books
    else:
        raise HTTPException(status_code=404, detail="Book not found")


@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: UUID, book: Book):
    for index, stored_book in enumerate(books_db):
        if stored_book.id == book_id:
            books_db[index] = book
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", response_model=Book)
async def delete_book(book_id: UUID):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            return books_db.pop(index)
    raise HTTPException(status_code=404, detail="Book not found")
