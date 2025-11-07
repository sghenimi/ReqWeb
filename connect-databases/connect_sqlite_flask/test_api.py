""" all users
curl http://localhost:8080/users
"""

""" get a user
curl http://localhost:8080/users/<user_id>
"""

""" add user
curl -X POST -H "Content-Type: application/json" -d '{"name":"John Doe","email":"johndoe@example.com"}' http://localhost:8080/users
"""

""" update user
curl -X PUT -H "Content-Type: application/json" -d '{"name":"Updated Name","email":"updated@example.com"}' http://localhost:8080/users/<user_id>
"""

""" delete user
curl -X DELETE http://localhost:8080/users/<user_id>
"""

