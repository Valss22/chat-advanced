import pytest
from src.app.main import app
from httpx import AsyncClient
import asyncio
from src.tests.db import test_metadata, test_engine


@pytest.fixture(scope='session')
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope='session', autouse=True)
def init_test_db():
    test_metadata.create_all(test_engine)
    yield
    test_metadata.drop_all(test_engine)
     

@pytest.fixture(scope='session')
async def client():
    async with AsyncClient(app=app, base_url='http://test') as client:
        yield client