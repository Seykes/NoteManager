from tortoise.models import Model
from tortoise import fields, queryset


class Note(Model):
    id = fields.IntField(pk=True)
    title = fields.TextField()
    text = fields.TextField()
    created = fields.DatetimeField(auto_now=True)


    def __str__(self):
        return self.title