def auth_token(client):
    client.post("/auth/register", json={"username": "bob", "password": "pw_bob"})
    res = client.post("/auth/token", data={"username": "bob", "password": "pw_bob"})
    return res.json()["access_token"]


def test_create_book(client):
    token = auth_token(client)
    book = {
        "title": "Test Book",
        "author": "Tester",
        "year": 2024,
        "description": "Test description"
    }
    res = client.post("/books/", json=book, headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    assert res.json()["title"] == "Test Book"

def test_get_books(client):
    token = auth_token(client)
    res = client.get("/books/", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    assert isinstance(res.json(), list)
