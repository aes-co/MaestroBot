import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.environ.get("MONGO_URL")
mongo = AsyncIOMotorClient(MONGO_URL)
db = mongo.maestrobot

# Setting per chat (grup/channel)
async def get_settings(chat_id):
    doc = await db.settings.find_one({"chat_id": str(chat_id)}) or {}
    return doc.get("settings", {})

async def set_setting(chat_id, key, value):
    await db.settings.update_one(
        {"chat_id": str(chat_id)},
        {"$set": {f"settings.{key}": value}},
        upsert=True
    )

async def get_setting(chat_id, key, default=None):
    doc = await db.settings.find_one({"chat_id": str(chat_id)}) or {}
    return doc.get("settings", {}).get(key, default)

# Setting global
async def get_global_setting(key, default=None):
    doc = await db.settings.find_one({"chat_id": "global"}) or {}
    return doc.get("settings", {}).get(key, default)

async def set_global_setting(key, value):
    await db.settings.update_one(
        {"chat_id": "global"},
        {"$set": {f"settings.{key}": value}},
        upsert=True
    )

# Sudo user management
async def add_sudo_user(user_id):
    await db.bot_settings.update_one(
        {"_id": "sudo"},
        {"$addToSet": {"users": user_id}},
        upsert=True
    )

async def remove_sudo_user(user_id):
    await db.bot_settings.update_one(
        {"_id": "sudo"},
        {"$pull": {"users": user_id}}
    )

async def get_sudo_users():
    doc = await db.bot_settings.find_one({"_id": "sudo"})
    return doc.get("users", []) if doc else []

# Volume khusus (contoh setting global)
async def set_default_volume(volume: int):
    await set_global_setting("default_volume", volume)

async def get_default_volume():
    return await get_global_setting("default_volume", 100)