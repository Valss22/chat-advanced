import pytest
from src.app.main import app
from httpx import AsyncClient
import asyncio
import databases
import sqlalchemy


DB_TEST_URL = 'postgresql://postgres:788556@localhost/chat_advanced_test'


@pytest.fixture(scope='session')
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope='session', autouse=True)
def init_test_db():
    db = databases.Database(DB_TEST_URL)
    metadata = sqlalchemy.MetaData()
    engine = sqlalchemy.create_engine(
        DB_TEST_URL, connect_args={}
    )
    metadata.create_all(engine)
    yield
    metadata.drop_all(engine)
     

@pytest.fixture(scope='session')
async def client():
    async with AsyncClient(app=app, base_url='http://test') as client:
        yield client