from maestrobot.startup.db_connections import mongo_db

COLLECTION = mongo_db.playlists

async def save_playlist(user_id: int, name: str, queue: list):
    await COLLECTION.update_one(
        {"_id": user_id},
        {"$set": {f"playlists.{name}": queue}},
        upsert=True
    )

async def get_playlists(user_id: int) -> dict:
    doc = await COLLECTION.find_one({"_id": user_id})
    return doc.get("playlists", {}) if doc else {}

async def get_playlist(user_id: int, name: str) -> list:
    doc = await COLLECTION.find_one({"_id": user_id})
    if not doc:
        return []
    return doc.get("playlists", {}).get(name, [])

async def delete_playlist(user_id: int, name: str) -> bool:
    result = await COLLECTION.update_one(
        {"_id": user_id},
        {"$unset": {f"playlists.{name}": ""}}
    )
    return result.modified_count > 0
