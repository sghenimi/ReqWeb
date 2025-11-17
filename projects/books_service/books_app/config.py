import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# ----- Config -----
APP_NAME = os.getenv("APP_NAME", "Book API")
APP_DEBUG = os.getenv("APP_DEBUG", "False") == "True"
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
SERVER_HOST = os.getenv("SERVER_HOST", "127.0.0.1")
SERVER_PORT = int(os.getenv("SERVER_PORT", 8000))
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./books.db")
