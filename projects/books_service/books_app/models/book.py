from sqlalchemy import Column, String, Integer
from uuid import uuid4
from books_app.database_books import Base

class BookModel(Base):
    __tablename__ = "books"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    title = Column(String, index=True)
    author = Column(String)
    year = Column(Integer, nullable=True)
    description = Column(String, nullable=True)
