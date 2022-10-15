import databases
import sqlalchemy
from src.app.main import app
from src.app.db import get_db

DB_TEST_URL = 'postgresql://postgres:788556@localhost/chat_advanced_test'


test_metadata = sqlalchemy.MetaData()
test_engine = sqlalchemy.create_engine(DB_TEST_URL)


async def get_test_db():
    try:
        test_db = databases.Database(DB_TEST_URL)
        await test_db.connect()
        yield test_db
    finally:
        await test_db.disconnect()


app.dependency_overrides[get_db] = get_test_db