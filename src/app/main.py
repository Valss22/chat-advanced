from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.app.db import init_db
from src.app.routers import api_router

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.on_event("startup")
def on_startup():
    init_db()
