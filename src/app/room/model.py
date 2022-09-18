from operator import mod
from statistics import mode
from tortoise import fields, models
from src.app.message.model import Message
from src.app.user.model import User


class Room(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ReverseRelation['User']
    message = fields.ReverseRelation['Message']


