from time import time
import jwt
from fastapi import HTTPException
from src.app.user.model import User
from src.app.user.schemas import *
from tortoise.exceptions import IntegrityError


TOKEN_TIME = 40_000
TOKEN_KEY = "ndg5P:,gr6K3?ug3ZdT@dD"


def get_token(username: str) -> str:
    payload = {
        "name": username,
        "exp": time() + TOKEN_TIME
    }
    return jwt.encode(payload, TOKEN_KEY)


async def create_user(user: UserIn) -> UserOut:
    try:
        new_user = await User.create(**user.dict())    
    except IntegrityError:
        raise HTTPException(
            status_code=400, 
            detail="User already exists"
        )
    token = get_token(user.dict()["name"])
    new_user_id = new_user.id
    return UserOut(id=new_user_id, token=token)


async def auth_user(user: UserIn) -> UserOut:
    user_in_db = await User.filter(name=user.dict()["name"]).first()
    if user_in_db:
        if user_in_db.password == user.dict()["password"]:
            token = get_token(user.dict()["name"])
            return UserOut(id=user_in_db.id, token=token)
        raise HTTPException(
            status_code=400,
            detail="Wrong password"
        )
    raise HTTPException(
        status_code=400,
        detail="User does not exist"
    )


async def get_user_by_name(name: str) -> UserDialogOut:
    user_in_db = await User.filter(name=name).first()
    if user_in_db:
        return user_in_db
    raise HTTPException(
        status_code=400,
        detail="User does not exist"
    )