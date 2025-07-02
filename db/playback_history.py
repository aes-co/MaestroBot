import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.environ.get("MONGO_URL")
mongo = AsyncIOMotorClient(MONGO_URL)
db = mongo.maestrobot

async def log_user_playback(user_id: int, song: dict):
    await db.playback_history.update_one(
        {"user_id": user_id},
        {"$push": {"songs": song}},
        upsert=True
    )

async def get_user_playback(user_id: int, limit: int = 20):
    doc = await db.playback_history.find_one({"user_id": user_id})
    return doc.get("songs", [])[-limit:] if doc and "songs" in doc else []