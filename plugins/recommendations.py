import random
from maestrobot.db.queues import db

async def get_playback_history(user_id: int, limit: int = 20):
    """
    Ambil riwayat pemutaran lagu user dari MongoDB untuk rekomendasi.
    """
    doc = await db.playback_history.find_one({"user_id": user_id})
    return doc.get("songs", [])[-limit:] if doc and "songs" in doc else []

async def log_playback(user_id: int, song: dict):
    """
    Simpan lagu yang diputar user (untuk rekomendasi/history).
    """
    await db.playback_history.update_one(
        {"user_id": user_id},
        {"$push": {"songs": song}},
        upsert=True
    )

async def recommend_songs(user_id: int, limit: int = 5):
    """
    Rekomendasi sederhana berdasarkan riwayat lagu user.
    Untuk demo: random shuffle dari history terakhir.
    """
    history = await get_playback_history(user_id, limit=30)
    if not history:
        return []
    # Ambil lagu unik, acak, dan batasi
    unique = {song["title"]: song for song in history}.values()
    recs = list(unique)
    random.shuffle(recs)
    return recs[:limit]

# Handler command /recommend (optional)
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

async def recommend_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    recs = await recommend_songs(user_id)
    if not recs:
        await update.message.reply_text("Belum ada riwayat lagu untuk rekomendasi.")
        return
    text = "🎵 Rekomendasi lagu untuk kamu:\n"
    for idx, song in enumerate(recs, 1):
        text += f"{idx}. <b>{song['title']}</b> — <i>{song.get('uploader','')}</i>\n"
    await update.message.reply_text(text, parse_mode="HTML")

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("recommend", recommend_command))