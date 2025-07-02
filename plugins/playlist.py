from maestrobot.db.queues import db

# === PLAYLIST PER USER (PERSISTENT) ===

async def add_to_playlist(user_id: int, song: dict):
    await db.user_playlists.update_one(
        {"user_id": user_id},
        {"$push": {"songs": song}},
        upsert=True
    )

async def get_playlist(user_id: int, limit: int = 20):
    doc = await db.user_playlists.find_one({"user_id": user_id})
    return doc.get("songs", [])[-limit:] if doc and "songs" in doc else []

async def remove_from_playlist(user_id: int, index: int):
    doc = await db.user_playlists.find_one({"user_id": user_id})
    if not doc or "songs" not in doc or index < 0 or index >= len(doc["songs"]):
        return False
    songs = doc["songs"]
    removed = songs.pop(index)
    await db.user_playlists.update_one(
        {"user_id": user_id},
        {"$set": {"songs": songs}}
    )
    return removed

async def clear_playlist(user_id: int):
    await db.user_playlists.update_one(
        {"user_id": user_id},
        {"$set": {"songs": []}}
    )

# === HANDLER COMMAND UNTUK PLAYLIST ===

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

async def playlist_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    playlist = await get_playlist(user_id)
    if not playlist:
        await update.message.reply_text("🎶 Playlist kamu kosong.")
        return
    text = "🎶 <b>Playlist Kamu:</b>\n"
    for idx, song in enumerate(playlist, 1):
        text += f"{idx}. <b>{song['title']}</b> — <i>{song.get('uploader','')}</i>\n"
    await update.message.reply_text(text, parse_mode="HTML")

async def addpl_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if not context.args:
        await update.message.reply_text("Kirim: /addpl <judul/link lagu>")
        return
    query = " ".join(context.args)
    from maestrobot.media.downloader import download_audio
    song = await download_audio(query)
    await add_to_playlist(user_id, song)
    await update.message.reply_text(f"✅ Ditambahkan ke playlist: <b>{song['title']}</b>", parse_mode="HTML")

async def removepl_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Kirim: /removepl <nomor_lagu>")
        return
    index = int(context.args[0]) - 1
    removed = await remove_from_playlist(user_id, index)
    if removed:
        await update.message.reply_text(f"❌ Dihapus dari playlist: <b>{removed['title']}</b>", parse_mode="HTML")
    else:
        await update.message.reply_text("Gagal menghapus. Pastikan nomor benar.")

async def clearpl_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    await clear_playlist(user_id)
    await update.message.reply_text("🎶 Playlist kamu dikosongkan.")

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("playlist", playlist_command))
    dispatcher.add_handler(CommandHandler("addpl", addpl_command))
    dispatcher.add_handler(CommandHandler("removepl", removepl_command))
    dispatcher.add_handler(CommandHandler("clearpl", clearpl_command))