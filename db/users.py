import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.environ.get("MONGO_URL")
mongo = AsyncIOMotorClient(MONGO_URL)
db = mongo.maestrobot

async def add_user(user_id: int, data: dict = None):
    data = data or {}
    await db.users.update_one(
        {"user_id": user_id},
        {"$setOnInsert": {"user_id": user_id, **data}},
        upsert=True
    )

async def get_user(user_id: int):
    return await db.users.find_one({"user_id": user_id})

async def update_user(user_id: int, update_data: dict):
    await db.users.update_one(
        {"user_id": user_id},
        {"$set": update_data},
        upsert=True
    )

async def get_all_users():
    return [u async for u in db.users.find({})]