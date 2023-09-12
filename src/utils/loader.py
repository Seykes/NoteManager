from src.db import db

from colorama import init as colorama_init

def start():
    colorama_init()
    db.init()


def close():
    db.close_connection()