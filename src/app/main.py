from databases import Database
from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from src.app.routers import api_router
from src.app.db import get_db

app = FastAPI()
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# @app.on_event('startup')
# async def startup(db: Database = Depends(get_db)):
#     await db.connect()


# @app.on_event('shutdown')
# async def shutdown(db: Database = Depends(get_db)):
#     await db.disconnect()

app.include_router(api_router)
