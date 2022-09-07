from time import time
import jwt
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.app.user.model import User
from src.app.user.schemas import UserIn, UserOut

TOKEN_TIME = 40_000
TOKEN_KEY = "ndg5P:,gr6K3?ug3ZdT@dD"


def get_token(username: str):
    payload = {
        "name": username,
        "exp": time() + TOKEN_TIME
    }
    return jwt.encode(payload, TOKEN_KEY)


def create_user(user: UserIn, db: Session) -> UserOut:
    db.add(User(**user.dict()))
    try:
        db.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=400, 
            detail="User already exists"
        )
    token = get_token(user.dict()["name"])
    user_id = db.query(User).\
    filter_by(name=user.dict()["name"]).first().id
    return UserOut(id=user_id, token=token)


def auth_user(user: UserIn, db: Session) -> UserOut:
    user_in_db = db.query(User).\
    filter_by(name=user.dict()["name"]).first()
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