import sqlite3

cnx = sqlite3.connect('db_bees.db')
cursor = cnx.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    email TEXT)''')

## Insert sample data into the "users" table
users = [
    ('Alpha Bin', 'alphbin@example.com'),
    ('John Doe', 'johndoe@example.com'),
    ('Jane Smith', 'janesmith@example.com'),
    ('Bob Johnson', 'bobjohnson@example.com')
]
cursor.executemany('INSERT INTO users (name, email) VALUES (?,?)', users)

## Commit the changes to the database
cnx.commit()

## Close the cursor and the database connection
cursor.close()
cnx.close()
