from .book import BookCreate
from .init_database import create_connection


def create_book(book: BookCreate):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (book.title, book.author))
    connection.commit()
    connection.close()

def get_all_books():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    connection.close()
    return books

def get_book_by_id(book_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()
    connection.close()
    return book

