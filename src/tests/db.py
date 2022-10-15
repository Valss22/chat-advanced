import databases
import sqlalchemy
from src.app.main import app
from src.app.db import db

DB_TEST_URL = 'postgresql://postgres:788556@localhost/chat_advanced_test'

test_db = databases.Database(DB_TEST_URL)
test_metadata = sqlalchemy.MetaData()
test_engine = sqlalchemy.create_engine(DB_TEST_URL)

app.dependency_overrides[db] = test_db