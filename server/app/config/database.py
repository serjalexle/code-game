from motor.motor_asyncio import AsyncIOMotorClient
from app.config.env import ENVSettings
from app.models.index import DB_MODELS
from beanie import init_beanie
from app.utils.logger import logger

from app.seeds.seed_admins import seed_admins


client = AsyncIOMotorClient(ENVSettings.get_db_url())
db = client[ENVSettings.DEFAULT_DB_NAME]


async def init_db():
    try:
        await init_beanie(db, document_models=DB_MODELS)
        logger.success("Database initialized successfully")

        await seed_admins()
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise


async def close_db():
    try:
        client.close()
        logger.success("Database connection closed successfully")
    except Exception as e:
        logger.error(f"Failed to close database connection: {e}")
        raise
