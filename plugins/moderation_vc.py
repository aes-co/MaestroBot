from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

from maestrobot.player import (
    skip,
    stop,
    pause,
    resume,
    get_active_track,
    is_playing,
    get_current_queue,
)
from maestrobot.db.queues import clear_queue

async def skip_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    await skip(chat_id)
    await update.message.reply_text("⏭ Lagu dilewati.")

async def pause_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    await pause(chat_id)
    await update.message.reply_text("⏸ VC dijeda.")

async def resume_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    await resume(chat_id)
    await update.message.reply_text("▶️ VC dilanjutkan.")

async def stop_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    await stop(chat_id)
    await update.message.reply_text("⏹ Voice Chat dihentikan dan keluar.")

async def status_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    track = get_active_track(chat_id)
    if not track:
        await update.message.reply_text("🎵 Tidak ada lagu yang sedang diputar.")
        return
    status = "⏸ Dijeda" if not is_playing(chat_id) else "▶️ Diputar"
    caption = f"{status}: <b>{track.get('title', 'Tanpa Judul')}</b>\n"
    caption += f"🎤 Oleh: {track.get('artist', 'Tidak diketahui')}"
    await update.message.reply_text(caption, parse_mode="HTML")

async def clear_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    await clear_queue(chat_id)
    await update.message.reply_text("🧹 Antrian lagu dibersihkan.")

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("skip", skip_command))
    dispatcher.add_handler(CommandHandler("pause", pause_command))
    dispatcher.add_handler(CommandHandler("resume", resume_command))
    dispatcher.add_handler(CommandHandler("stopvc", stop_command))
    dispatcher.add_handler(CommandHandler("vcstatus", status_command))
    dispatcher.add_handler(CommandHandler("clearqueue", clear_command))
