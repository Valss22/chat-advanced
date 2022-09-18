from tortoise import fields, models

class Message(models.Model):
    id = fields.IntField(pk=True)
    text = fields.TextField()
    user = fields.ForeignKeyField('models.User', related_name='message')
    room = fields.ForeignKeyField('models.Room', related_name='message')
