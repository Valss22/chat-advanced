from fastapi import APIRouter
from src.app.user.schemas import *
from src.app.user.services import UserService
from fastapi import Depends
from databases import Database
from src.app.db import get_db

user_router = APIRouter(
    prefix='/user'
)


@user_router.post('/register/', response_model=UserOut)
async def register_user(
    user: UserIn, 
    db: Database = Depends(get_db),
    user_service: UserService = Depends()
):
    return await user_service.create_user(user, db)


@user_router.post('/login/', response_model=UserOut)
async def login_user(
    user: UserIn,
    db: Database = Depends(get_db), 
    user_service: UserService = Depends()
):
    return await user_service.auth_user(user, db)


@user_router.get('/', response_model=UserDialogOut)
async def get_user(
    name: str,
    db: Database = Depends(get_db),
    user_service: UserService = Depends()
):
    return await user_service.get_user_by_name(name, db)

