import databases
import sqlalchemy
from src.app.main import app


DB_URL = "sqlite:///./test.db"

db = databases.Database(DB_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DB_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)