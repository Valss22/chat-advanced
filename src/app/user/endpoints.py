from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.app.db import get_db
from src.app.user.schemas import UserIn, UserOut
from src.app.user.services import auth_user, create_user

user_router = APIRouter(
    prefix="/user"
)


@user_router.post("/register/", response_model=UserOut)
def register_user(user: UserIn, db: Session = Depends(get_db)):
    return create_user(user, db)


@user_router.post("/login/", response_model=UserOut)
def login_user(user: UserIn, db: Session = Depends(get_db)):
    return auth_user(user, db)
