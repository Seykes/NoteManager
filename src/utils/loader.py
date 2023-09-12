"""
Module for storage start and close fucntions
"""


from colorama import init as colorama_init
from src.db import db


def start():
    """
    Initialize colorama and database
    """
    colorama_init()
    db.init()


def close():
    db.close_connection()
    