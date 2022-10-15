import databases
import sqlalchemy


DB_URL = 'postgresql://postgres:788556@localhost/chat_advanced'

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DB_URL)
metadata.create_all(engine)

db = databases.Database(DB_URL)

def get_db():
    return db

