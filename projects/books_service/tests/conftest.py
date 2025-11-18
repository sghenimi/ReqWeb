import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from books_app.core.database_books import Base
from books_app.core.app import create_app
# from books_app.core.database_books import SessionLocal
# from books_app.core import database


# Nouvelle base SQLite en mémoire pour les tests
TEST_DATABASE_URL = "sqlite:///./tests_books.db"

engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Override dependency get_db
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    # Création des tables pour les tests
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


@pytest.fixture
def client():
    app = create_app()

    # Override de la dépendance get_db pour utiliser la BD de test
    from books_app.routers import auth, books

    app.dependency_overrides[auth.get_db] = override_get_db
    app.dependency_overrides[books.get_db] = override_get_db

    return TestClient(app)
