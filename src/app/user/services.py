from time import time
import jwt
from fastapi import HTTPException
from src.app.user.model import users
from src.app.user.schemas import *
from src.app.db import db
import sqlalchemy

TOKEN_TIME = 40_000
TOKEN_KEY = 'ndg5P:,gr6K3?ug3ZdT@dD'


class UserService:
    
    def get_token(self, username: str) -> str:
        payload = {
            'name': username,
            'exp': time() + TOKEN_TIME
        }
        return jwt.encode(payload, TOKEN_KEY)


    async def create_user(self, user: UserIn) -> UserOut:
        try:
            new_user = users.insert().values(**user.dict())
            new_user_id = await db.execute(new_user)
        except sqlalchemy.exc.IntegrityError:
            raise HTTPException(
                status_code=400, 
                detail='User already exists'
            )
        token = self.get_token(user.name)
        return UserOut(id=new_user_id, token=token)


    async def auth_user(self, user: UserIn) -> UserOut:
        user_query = users.select().where(users.c.name == user.name)
        user_in_db = await db.fetch_one(user_in_db)
        if user_in_db:
            if user_in_db.password == user.password:
                token = self.get_token(user.dict()['name'])
                return UserOut(id=user_in_db.id, token=token)
            raise HTTPException(
                status_code=400,
                detail='Wrong password'
            )
        raise HTTPException(
            status_code=400,
            detail='User does not exist'
        )


    async def get_user_by_name(self, name: str) -> UserDialogOut:
        user_query = users.select().where(users.c.name == name)
        user_in_db = await db.fetch_one(user_query)
        if user_in_db:
            return user_in_db
        raise HTTPException(
            status_code=400,
            detail='User does not exist'
        )