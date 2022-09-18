from tortoise.contrib.fastapi import register_tortoise
from src.app.main import app

DB_URL = "postgresql://postgres:788556@localhost/chat_advanced"

APP_MODELS = [
    "src.app.user.model",
    "src.app.message.model",
    "src.app.room.model",
]

register_tortoise(
    app,
    db_url=DB_URL,
    modules={"models": APP_MODELS},
    generate_schemas=True,
    add_exception_handlers=True,
)