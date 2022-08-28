from time import time
import jwt
from sqlalchemy.orm import Session
from src.app.user.model import User
from src.app.user.schemas import UserIn, UserOut

TOKEN_TIME = 40_000
TOKEN_KEY = "ndg5P:,gr6K3?ug3ZdT@dD"


def get_token(user_id: str, username: str):
    payload = {
        "id": str(user_id),
        "name": username,
        "exp": time() + TOKEN_TIME
    }
    return jwt.encode(payload, TOKEN_KEY)


def create_user(user: UserIn, db: Session) -> UserOut:
    db.add(User(**user.dict()))
    db.commit()
    print(db.query(User).all())
    return UserOut(id=1, token="32")
    # return UserOut(id=db.query(User).all().last())
