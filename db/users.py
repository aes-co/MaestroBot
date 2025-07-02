import os
from motor.motor_asyncio import AsyncIOMotorClient

mongo_url = os.getenv("MONGO_URL")
mongo_client = AsyncIOMotorClient(mongo_url)
db = mongo_client.maestrobot

async def get_user(user_id: int):
    doc = await db.users.find_one({"user_id": user_id})
    return doc if doc else {}

async def add_or_update_user(user: dict):
    await db.users.update_one(
        {"user_id": user["user_id"]},
        {"$set": user},
        upsert=True
    )

async def get_total_users():
    return await db.users.count_documents({})

async def get_all_users():
    cursor = db.users.find()
    return [user async for user in cursor]
