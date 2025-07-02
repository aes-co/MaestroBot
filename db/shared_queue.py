from maestrobot.startup.db_connections import mongo_db

COLLECTION = mongo_db.shared_queues

async def save_shared_queue(name: str, tracks: list, owner_id: int):
    await COLLECTION.update_one(
        {"_id": name},
        {"$set": {"tracks": tracks, "owner_id": owner_id}},
        upsert=True
    )

async def load_shared_queue(name: str) -> list:
    doc = await COLLECTION.find_one({"_id": name})
    return doc.get("tracks", []) if doc else []

async def delete_shared_queue(name: str, requester_id: int) -> bool:
    doc = await COLLECTION.find_one({"_id": name})
    if doc and doc.get("owner_id") == requester_id:
        await COLLECTION.delete_one({"_id": name})
        return True
    return False

async def list_shared_queues() -> list:
    cursor = COLLECTION.find({}, {"_id": 1, "owner_id": 1})
    return await cursor.to_list(length=100)
