from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.app.main import app
from src.app.db import get_db
from fastapi.testclient import TestClient


DATABASE_TEST_URL = "postgresql://postgres:788556@localhost/chat_advanced_test/"
engine = create_engine(
    DATABASE_TEST_URL
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_test_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = get_test_db
client = TestClient(app)

def test_create_user():
    pass