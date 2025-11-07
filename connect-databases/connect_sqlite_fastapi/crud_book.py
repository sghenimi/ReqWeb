from .book import BookCreate
from .init_database import create_connection


def create_book(book: BookCreate):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (book.title, book.author))
    connection.commit()
    connection.close()
