def test_register_user(client):
    data = {
        "username": "alice",
        "password": "pw_alice"
    }
    response = client.post("/auth/register", json=data)
    assert response.status_code == 200
    assert response.json()["username"] == "alice"


def test_login(client):
    response = client.post(
        "/auth/token",
        data={"username": "alice", "password": "pw_alice"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_access_protected_route(client):
    response = client.post(
        "/auth/token",
        data={"username": "alice", "password": "pw_alice"}
    )
    token = response.json()["access_token"]

    protected = client.get(
        "/books/",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert protected.status_code == 200
