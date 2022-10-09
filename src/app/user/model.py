import sqlalchemy
from src.app.db import metadata


users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(255), unique=True),
    sqlalchemy.Column('password', sqlalchemy.String(255)),
    sqlalchemy.Column('message', sqlalchemy.Integer, sqlalchemy.ForeignKey('messages.id'))
)
