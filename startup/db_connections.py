import motor.motor_asyncio
import redis.asyncio as aioredis
from maestrobot.configs import MONGO_URI, REDIS_URI

mongo_client = None
redis_client = None

async def init_databases():
    global mongo_client, redis_client
    mongo_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
    redis_client = aioredis.from_url(REDIS_URI, decode_responses=True)
    # Test connections
    await redis_client.ping()
    await mongo_client.admin.command('ping')