from pydantic import BaseModel


class UserIn(BaseModel):
    name: str
    password: str


class UserOut(BaseModel):
    id: int
    token: str
