from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.app.db import get_db
from src.app.user.schemas import CreateUserModel
from src.app.user.services import create_user

user_router = APIRouter(
    prefix="/user"
)


@user_router.post("/register/")
def register_user(user: CreateUserModel, db: Session = Depends(get_db)):
    return create_user(user, db)
