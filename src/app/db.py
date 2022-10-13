import databases
import sqlalchemy


DB_URL = 'postgresql://postgres:788556@localhost/chat_advanced'

db = databases.Database(DB_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DB_URL, connect_args={}
)
metadata.create_all(engine)