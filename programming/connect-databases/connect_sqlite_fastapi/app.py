import uvicorn
from fastapi import FastAPI
from connect_sqlite_fastapi.book import BookCreate, Book
from connect_sqlite_fastapi.crud_book import create_book, get_all_books

app = FastAPI()

@app.get("/")
def read_root():
 return {"message": "Welcome !"}

@app.get('/books')
def get_all_users():
    books = get_all_books()

    return {"books": books}

@app.post("/books/new")
def create_book_endpoint(book: BookCreate):
 book_id = create_book(book)
 return {"id": book_id, **book.dict()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)