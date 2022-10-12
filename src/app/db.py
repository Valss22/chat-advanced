import databases
import sqlalchemy
from src.app.main import app


DB_URL = 'postgres://postgres:788556@localhost/chat_advanced'

db = databases.Database(DB_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DB_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)