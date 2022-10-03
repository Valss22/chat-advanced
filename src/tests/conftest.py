import pytest
from src.app.main import app
from httpx import AsyncClient
import asyncio
from tortoise import Tortoise
from src.app.db import APP_MODELS


DB_TEST_URL = 'postgres://postgres:788556@localhost/chat_advanced_test'


@pytest.fixture(scope='session')
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope='session', autouse=True)
async def init_test_db():
    await Tortoise.init(
        db_url=DB_TEST_URL,
        modules={'models': APP_MODELS},
        _create_db=True,
    )
    await Tortoise.generate_schemas()
    yield
    await Tortoise._drop_databases()
     

@pytest.fixture(scope='session')
async def client():
    async with AsyncClient(app=app, base_url='http://test') as client:
        yield client