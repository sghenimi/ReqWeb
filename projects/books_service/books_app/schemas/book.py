from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class Book(BaseModel):
    id: UUID
    title: str
    author: str
    year: Optional[int] = None
    description: Optional[str] = None

    class Config:
        from_attributes = True


class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int] = None
    description: Optional[str] = None


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    description: Optional[str] = None

class BooksResponse(BaseModel):
    total: int
    items: list[Book]
