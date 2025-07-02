import motor.motor_asyncio
import redis.asyncio as aioredis
from maestrobot.configs import MONGO_URI, REDIS_URI
from maestrobot.db import settings as db_settings

mongo_client = None
redis_client = None

async def init_databases():
    global mongo_client, redis_client
    mongo_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
    redis_client = aioredis.from_url(REDIS_URI, decode_responses=True)
    await redis_client.ping()
    await mongo_client.admin.command('ping')
    await db_settings.init_settings_collection()
