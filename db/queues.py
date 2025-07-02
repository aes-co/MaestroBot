import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.environ.get("MONGO_URL")
mongo = AsyncIOMotorClient(MONGO_URL)
db = mongo.maestrobot

# ===== QUEUE PER CHAT (untuk antrian lagu di setiap grup/channel) =====

async def add_to_queue(chat_id: int, song: dict):
    await db.queues.update_one(
        {"chat_id": str(chat_id)},
        {"$push": {"songs": song}},
        upsert=True
    )

async def get_queue(chat_id: int):
    doc = await db.queues.find_one({"chat_id": str(chat_id)})
    return doc.get("songs", []) if doc and "songs" in doc else []

async def pop_queue(chat_id: int):
    doc = await db.queues.find_one({"chat_id": str(chat_id)})
    if doc and "songs" in doc and doc["songs"]:
        # Pop lagu terdepan
        song = doc["songs"][0]
        await db.queues.update_one(
            {"chat_id": str(chat_id)},
            {"$pop": {"songs": -1}}
        )
        return song
    return None

async def clear_queue(chat_id: int):
    await db.queues.update_one(
        {"chat_id": str(chat_id)},
        {"$set": {"songs": []}}
    )

async def remove_from_queue(chat_id: int, index: int):
    doc = await db.queues.find_one({"chat_id": str(chat_id)})
    if not doc or "songs" not in doc or index < 0 or index >= len(doc["songs"]):
        return False
    songs = doc["songs"]
    removed = songs.pop(index)
    await db.queues.update_one(
        {"chat_id": str(chat_id)},
        {"$set": {"songs": songs}}
    )
    return removed

# ===== PLAYBACK HISTORY UNTUK REKOMENDASI =====

async def log_playback(chat_id: int, song: dict):
    await db.group_playback_history.update_one(
        {"chat_id": str(chat_id)},
        {"$push": {"songs": song}},
        upsert=True
    )

async def get_playback_history(chat_id: int, limit: int = 20):
    doc = await db.group_playback_history.find_one({"chat_id": str(chat_id)})
    return doc.get("songs", [])[-limit:] if doc and "songs" in doc else []