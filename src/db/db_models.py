"""
Module for storage database models
"""

from tortoise import fields
from tortoise.models import Model


class Note(Model):
    """
    Base note model
    """
    id = fields.IntField(pk=True)
    title = fields.TextField()
    text = fields.TextField()
    created = fields.DatetimeField(auto_now=True)


    def __str__(self):
        return self.title
    