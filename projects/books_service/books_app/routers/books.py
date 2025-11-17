from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from uuid import UUID
from books_app.database_books import SessionLocal
from books_app.models.book import BookModel
from books_app.schemas.book import Book, BookCreate, BookUpdate
from books_app.utils.normalize import normalize

router = APIRouter(prefix="/books", tags=["Books"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----- GET with pagination -----
@router.get("/", response_model=list[Book])
def get_books(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50)
):
    offset = (page - 1) * limit
    return db.query(BookModel).offset(offset).limit(limit).all()


# ----- Search -----
@router.get("/search/{title}", response_model=list[Book])
def search_books(title: str, db: Session = Depends(get_db)):
    normalized_query = normalize(title)

    books = db.query(BookModel).all()
    results = [b for b in books if normalized_query in normalize(b.title)]

    if not results:
        raise HTTPException(status_code=404, detail="No books found matching title")

    return results


# ----- Create -----
@router.post("/", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = BookModel(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


# ----- Update -----
@router.put("/{book_id}", response_model=Book)
def update_book(book_id: UUID, data: BookUpdate, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == str(book_id)).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(book, field, value)

    db.commit()
    db.refresh(book)
    return book


# ----- Delete -----
@router.delete("/{book_id}")
def delete_book(book_id: UUID, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == str(book_id)).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}
