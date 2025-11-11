from fastapi.testclient import TestClient

from projects.books_service.books_app.main import app, books_db, Book, uuid4

client  = TestClient(app)

# ----- Helper -----
def get_first_book():
    return books_db[0]

# ----- Tests -----
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_get_books_pagination():
    response = client.get("/books?page=1&limit=2")
    assert response.status_code == 200
    books = response.json()
    assert len(books) == 2

def test_search_books_without_accents():
    response = client.get("/books/search/etranger")
    assert response.status_code == 200
    data = response.json()
    assert any("Étranger" in b["title"] or "Etranger" in b["title"] for b in data)

def test_create_book():
    new_book = {
        "id": str(uuid4()),
        "title": "Nouveau Livre",
        "author": "Auteur Inconnu",
        "year": 2025,
        "description": "Un livre de test."
    }
    response = client.post("/books/", json=new_book)
    assert response.status_code == 200
    assert response.json()["title"] == "Nouveau Livre"

def test_update_book():
    book = get_first_book()
    updated_data = {"description": "Description mise à jour"}
    response = client.put(f"/books/{book.id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["description"] == "Description mise à jour"

def test_delete_book():
    # Crée un livre temporaire
    temp_book = Book(
        id=uuid4(),
        title="Livre Temporaire",
        author="Auteur Temp",
        year=2024,
        description="À supprimer"
    )
    books_db.append(temp_book)

    response = client.delete(f"/books/{temp_book.id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Book deleted successfully"

    # Vérifie qu'il n'est plus dans la liste
    assert all(b.id != temp_book.id for b in books_db)
