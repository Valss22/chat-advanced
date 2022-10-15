import databases
import sqlalchemy


DB_URL = 'postgresql://postgres:788556@localhost/chat_advanced'

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DB_URL)
metadata.create_all(engine)


async def get_db():
    try:
        db = databases.Database(DB_URL)
        await db.connect()
        yield db
    finally:
        await db.disconnect()
    

