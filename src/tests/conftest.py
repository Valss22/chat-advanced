import pytest
from src.tests.db import engine
from src.app.db import Base
from src.app.main import app
from fastapi.testclient import TestClient
from src.tests.db import get_test_db


@pytest.fixture(scope="session", autouse=True)
def init_test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
     

@pytest.fixture(scope="session")
def client():
    with TestClient(app=app, base_url="http://test") as client:
        yield client