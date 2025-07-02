from maestrobot.startup.db_connections import mongo_db

COLLECTION = mongo_db.playback_history

async def log_playback(user_id: int, song: dict):
    await COLLECTION.update_one(
        {"user_id": user_id},
        {"$push": {"songs": song}},
        upsert=True
    )

async def get_user_history(user_id: int, limit: int = 20):
    doc = await COLLECTION.find_one({"user_id": user_id})
    return doc.get("songs", [])[-limit:] if doc else []
