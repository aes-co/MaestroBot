import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.environ.get("MONGO_URL")
mongo = AsyncIOMotorClient(MONGO_URL)
db = mongo.maestrobot

# === FUNGSI PERSISTENT ANTRIAN GLOBAL ===
async def add_to_shared_queue(song: dict):
    await db.shared_queue.update_one(
        {"_id": "global"},
        {"$push": {"songs": song}},
        upsert=True
    )

async def get_shared_queue():
    doc = await db.shared_queue.find_one({"_id": "global"})
    return doc.get("songs", []) if doc and "songs" in doc else []

async def pop_shared_queue():
    doc = await db.shared_queue.find_one({"_id": "global"})
    if doc and "songs" in doc and doc["songs"]:
        song = doc["songs"][0]
        await db.shared_queue.update_one(
            {"_id": "global"},
            {"$pop": {"songs": -1}}
        )
        return song
    return None

async def clear_shared_queue():
    await db.shared_queue.update_one(
        {"_id": "global"},
        {"$set": {"songs": []}}
    )

# === HANDLER COMMAND UNTUK ADMIN/OWNER ===
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from maestrobot.configs import OWNER_ID, SUDO_USERS

def is_owner_or_sudo(user_id):
    return str(user_id) == str(OWNER_ID) or user_id in SUDO_USERS

async def sharedqueue_command(update: Update, context: CallbackContext):
    queue = await get_shared_queue()
    if not queue:
        await update.message.reply_text("🌐 Antrian global kosong.")
        return
    text = "🌐 <b>Antrian Global:</b>\n"
    for idx, song in enumerate(queue, 1):
        text += f"{idx}. <code>{song['title']}</code> — <i>{song.get('uploader','')}</i>\n"
    await update.message.reply_text(text, parse_mode="HTML")

async def addglobal_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if not is_owner_or_sudo(user_id):
        await update.message.reply_text("❌ Hanya owner/sudo yang bisa menambah antrian global.")
        return
    if not context.args:
        await update.message.reply_text("Kirim: /addglobal <judul/link lagu>")
        return
    query = " ".join(context.args)
    # Gunakan downloader asli
    from maestrobot.media.downloader import download_audio
    song = await download_audio(query)
    await add_to_shared_queue(song)
    await update.message.reply_text(f"✅ Ditambahkan ke antrian global: <b>{song['title']}</b>", parse_mode="HTML")

async def popglobal_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if not is_owner_or_sudo(user_id):
        await update.message.reply_text("❌ Hanya owner/sudo yang bisa mengambil dari antrian global.")
        return
    song = await pop_shared_queue()
    if song:
        await update.message.reply_text(f"⏭️ Lagu diambil dari antrian global: <b>{song['title']}</b>", parse_mode="HTML")
    else:
        await update.message.reply_text("🌐 Antrian global kosong.")

async def clearglobal_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if not is_owner_or_sudo(user_id):
        await update.message.reply_text("❌ Hanya owner/sudo yang bisa mengosongkan antrian global.")
        return
    await clear_shared_queue()
    await update.message.reply_text("🌐 Antrian global dikosongkan.")

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("sharedqueue", sharedqueue_command))
    dispatcher.add_handler(CommandHandler("addglobal", addglobal_command))
    dispatcher.add_handler(CommandHandler("popglobal", popglobal_command))
    dispatcher.add_handler(CommandHandler("clearglobal", clearglobal_command))