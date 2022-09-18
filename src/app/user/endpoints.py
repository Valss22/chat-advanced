from fastapi import APIRouter
from src.app.user.schemas import *
from src.app.user.services import auth_user, create_user, get_user_by_name


user_router = APIRouter(
    prefix="/user"
)


@user_router.post("/register/", response_model=UserOut)
async def register_user(user: UserIn):
    return await create_user(user)


@user_router.post("/login/", response_model=UserOut)
async def login_user(user: UserIn):
    return await auth_user(user)


@user_router.get("/", response_model=UserDialogOut)
async def get_user(name: str):
    return await get_user_by_name(name)

