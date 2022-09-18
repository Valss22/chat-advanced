from tortoise import fields, models
from src.app.message.model import Message


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    message = fields.ReverseRelation['Message']