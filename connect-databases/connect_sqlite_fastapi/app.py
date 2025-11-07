import uvicorn
from fastapi import FastAPI
from .book import Book, BookCreate
from .crud_book import create_book

app = FastAPI()

@app.get("/")
def read_root():
 return {"message": "Welcome !"}

@app.post("/books/")
def create_book_endpoint(book: BookCreate):
 book_id = create_book(book)
 return {"id": book_id, **book.dict()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)