from fastapi import APIRouter
from src.app.user.schemas import *
from src.app.user.services import UserService
from fastapi import Depends


user_router = APIRouter(
    prefix='/user'
)


@user_router.post('/register/', response_model=UserOut)
async def register_user(
    user: UserIn, 
    user_service: UserService = Depends()
):
    return await user_service.create_user(user)


@user_router.post('/login/', response_model=UserOut)
async def login_user(
    user: UserIn, 
    user_service: UserService = Depends()
):
    return await user_service.auth_user(user)


@user_router.get('/', response_model=UserDialogOut)
async def get_user(
    name: str, 
    user_service: UserService = Depends()
):
    return await user_service.get_user_by_name(name)

