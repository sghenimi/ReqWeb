import sys
from pathlib import Path

from flask import Flask, jsonify, request
from flasgger import Swagger
import sqlite3

app = Flask(__name__)

template = {
    "swagger": "2.0",
    "info": {
        "title": "Flask API",
        "description": "This API using Python Flask",
        "version": "1.0"
    }
}
app.config['SWAGGER'] = {
    'title': 'Flask API',
    'uiversion': 2,
    'template': './resources/flasgger/swagger_ui.html'
}
Swagger(app, template=template)


@app.route('/users', methods=['GET'])
def get_all_users():
    ## Connect to the database
    conn = sqlite3.connect('db_bees.db')
    cursor = conn.cursor()

    ## Execute the SQL query to retrieve all users
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    ## Close the cursor and the database connection
    cursor.close()
    conn.close()

    ## Return the users as JSON
    return jsonify(users)


## Endpoint to retrieve a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    ## Connect to the database
    conn = sqlite3.connect('db_bees.db')
    cursor = conn.cursor()

    ## Execute the SQL query to retrieve the user by ID
    cursor.execute('SELECT * FROM users WHERE id =?', (user_id,))
    user = cursor.fetchone()

    ## Close the cursor and the database connection
    cursor.close()
    conn.close()

    ## Check if the user exists
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404


## Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    ## Get the user data from the request body
    data = request.get_json()
    name = data['name']
    email = data['email']

    ## Connect to the database
    conn = sqlite3.connect('db_bees.db')
    cursor = conn.cursor()

    ## Execute the SQL query to insert a new user
    cursor.execute('INSERT INTO users (name, email) VALUES (?,?)', (name, email))
    conn.commit()

    ## Close the cursor and the database connection
    cursor.close()
    conn.close()

    ## Return a success message
    return jsonify({'message': 'User created successfully'})


## Endpoint to update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    ## Get the updated user data from the request body
    data = request.get_json()
    name = data['name']
    email = data['email']

    ## Connect to the database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    ## Execute the SQL query to update the user
    cursor.execute('UPDATE users SET name =?, email =? WHERE id =?', (name, email, user_id))
    conn.commit()

    ## Close the cursor and the database connection
    cursor.close()
    conn.close()

    ## Return a success message
    return jsonify({'message': 'User updated successfully'})


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = sqlite3.connect('db_bees.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id =?', (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception:
        port = 8080
    app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)
