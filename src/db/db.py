from tortoise import Tortoise, run_async


async def init_schemas():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["src.db.db_models"]}
        )
    
    await Tortoise.generate_schemas()
    
    
async def close():
    await Tortoise.close_connections()

def close_connection():
    run_async(close())

def init():
    run_async(init_schemas())