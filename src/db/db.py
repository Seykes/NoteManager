"""
Module to storage base database functions, like init and close
"""

from tortoise import Tortoise, run_async


async def init_schemas():
    """
    Initialization of database schemas
    """
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["src.db.db_models"]}
        )
    await Tortoise.generate_schemas()
    
async def close():
    """
    Close database connection
    """
    await Tortoise.close_connections()

def close_connection():
    """
    Async start for closing database connection
    """
    run_async(close())

def init():
    """
    Async start for initialization schemas
    """
    run_async(init_schemas())
