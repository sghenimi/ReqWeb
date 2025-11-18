from sqlalchemy import Column, String
from books_app.core.database_books import Base
import uuid

class UserModel(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user")  # e.g. "user" or "admin"
