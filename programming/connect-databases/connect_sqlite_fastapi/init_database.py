import sqlite3


def create_connection():
    connection = sqlite3.connect("books.db")
    return connection


def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS books (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     title TEXT NOT NULL,
     author TEXT NOT NULL
     )
     """)
    connection.commit()
    connection.close()


create_table()  # Call this function to create the table
