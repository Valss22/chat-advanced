from sqlalchemy.orm import Session

from src.app.user.model import User
from src.app.user.schemas import CreateUserModel


def check_user(name: str,  db: Session):
    if db.query(User).filter_by(name=name):
        pass


def create_user(user: CreateUserModel, db: Session):
    db.add(User(name=user.dict()["name"], password=user.dict()["password"]))
    db.commit()
