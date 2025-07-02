import os
from motor.motor_asyncio import AsyncIOMotorClient

mongo_url = os.getenv("MONGO_URL")
mongo_client = AsyncIOMotorClient(mongo_url)
db = mongo_client.maestrobot

queue_cache = {}

async def get_queue(chat_id: int):
    if chat_id in queue_cache:
        return queue_cache[chat_id]
    doc = await db.queues.find_one({"chat_id": chat_id})
    queue = doc["songs"] if doc and "songs" in doc else []
    queue_cache[chat_id] = queue
    return queue

async def add_to_queue(chat_id: int, song: dict):
    queue = await get_queue(chat_id)
    queue.append(song)
    queue_cache[chat_id] = queue
    await db.queues.update_one(
        {"chat_id": chat_id},
        {"$set": {"songs": queue}},
        upsert=True
    )

async def pop_next_song(chat_id: int):
    queue = await get_queue(chat_id)
    if not queue:
        return None
    next_song = queue.pop(0)
    queue_cache[chat_id] = queue
    await db.queues.update_one(
        {"chat_id": chat_id},
        {"$set": {"songs": queue}},
        upsert=True
    )
    return next_song

async def clear_queue(chat_id: int):
    queue_cache.pop(chat_id, None)
    await db.queues.update_one(
        {"chat_id": chat_id},
        {"$set": {"songs": []}},
        upsert=True
    )
