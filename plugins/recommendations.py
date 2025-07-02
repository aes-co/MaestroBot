import random
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from maestrobot.db.playback_history import get_user_history, log_playback
from maestrobot.player import add_to_queue

async def recommend_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    history = await get_user_history(user_id, limit=30)
    if not history:
        await update.message.reply_text("Belum ada riwayat lagu untuk rekomendasi.")
        return

    unique = {song["title"]: song for song in history}.values()
    recs = list(unique)
    random.shuffle(recs)
    selected = recs[:5]

    text = "🎵 <b>Rekomendasi lagu untuk kamu:</b>\n\n"
    for idx, song in enumerate(selected, 1):
        title = song.get("title", "Tanpa Judul")
        artist = song.get("uploader", "Tidak diketahui")
        text += f"{idx}. <b>{title}</b> — <i>{artist}</i>\n"
        await add_to_queue(chat_id, song)

    await update.message.reply_text(text, parse_mode="HTML")

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("recommend", recommend_command))
