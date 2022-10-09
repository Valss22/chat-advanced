from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.app.routers import api_router
from src.app.db import db

app = FastAPI()
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.on_event('startup')
async def startup():
    await db.connect()


@app.on_event('shutdown')
async def shutdown():
    await db.disconnect()

app.include_router(api_router)
