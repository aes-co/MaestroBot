import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.environ.get("MONGO_URL")
mongo = AsyncIOMotorClient(MONGO_URL)
db = mongo.maestrobot
settings_col = db.settings
bot_settings_col = db.bot_settings

async def init_settings_collection():
    await settings_col.create_index("chat_id", unique=True)
    await bot_settings_col.create_index("_id", unique=True)

async def get_setting(chat_id, key, default=None):
    doc = await settings_col.find_one({"chat_id": str(chat_id)})
    return doc.get("settings", {}).get(key, default) if doc else default

async def set_setting(chat_id, key, value):
    await settings_col.update_one(
        {"chat_id": str(chat_id)},
        {"$set": {f"settings.{key}": value}},
        upsert=True
    )

async def get_global_setting(key, default=None):
    doc = await settings_col.find_one({"chat_id": "global"})
    return doc.get("settings", {}).get(key, default) if doc else default

async def set_global_setting(key, value):
    await settings_col.update_one(
        {"chat_id": "global"},
        {"$set": {f"settings.{key}": value}},
        upsert=True
    )

async def get_settings(chat_id):
    doc = await settings_col.find_one({"chat_id": str(chat_id)})
    return doc.get("settings", {}) if doc else {}

async def add_sudo_user(user_id):
    await bot_settings_col.update_one(
        {"_id": "sudo"},
        {"$addToSet": {"users": user_id}},
        upsert=True
    )

async def remove_sudo_user(user_id):
    await bot_settings_col.update_one(
        {"_id": "sudo"},
        {"$pull": {"users": user_id}}
    )

async def get_sudo_users():
    doc = await bot_settings_col.find_one({"_id": "sudo"})
    return doc.get("users", []) if doc else []

async def set_default_volume(volume):
    await set_global_setting("default_volume", volume)

async def get_default_volume():
    return await get_global_setting("default_volume", 100)
