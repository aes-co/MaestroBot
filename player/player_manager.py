from maestrobot.db.queues import (
    add_to_queue,
    get_queue,
    pop_queue,
    clear_queue,
    log_playback
)
from maestrobot.db.settings import get_setting
from maestrobot.media.downloader import download_audio

# Fungsi utama untuk mengelola player/antrian VC

async def play_song(chat_id: int, query: str, user_id: int = None):
    """
    Download lagu dan tambahkan ke antrian, otomatis play jika kosong.
    """
    # Download lagu
    song = await download_audio(query)
    # Masukkan ke queue
    await add_to_queue(chat_id, song)
    # Log history playback user (opsional)
    if user_id:
        await log_playback(user_id, song)
    return song

async def get_current_queue(chat_id: int):
    """
    Ambil antrian lagu saat ini untuk grup.
    """
    return await get_queue(chat_id)

async def skip_song(chat_id: int):
    """
    Hapus lagu terdepan dari antrian dan return lagu selanjutnya.
    """
    await pop_queue(chat_id)
    queue = await get_queue(chat_id)
    return queue[0] if queue else None

async def clear_all_queue(chat_id: int):
    """
    Kosongkan seluruh antrian lagu grup.
    """
    await clear_queue(chat_id)

async def now_playing(chat_id: int):
    """
    Info lagu yang sedang diputar.
    """
    queue = await get_queue(chat_id)
    return queue[0] if queue else None

# Handler Telegram (bisa dipisah ke handlers/player_commands.py)
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

async def play_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    if not context.args:
        await update.message.reply_text("Kirim: /play <judul/link lagu>")
        return
    query = " ".join(context.args)
    song = await play_song(chat_id, query, user_id)
    await update.message.reply_text(f"▶️ Ditambahkan: <b>{song['title']}</b>\n{song.get('webpage_url','')}", parse_mode="HTML")

async def queue_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    queue = await get_current_queue(chat_id)
    if not queue:
        await update.message.reply_text("📭 Antrian kosong.")
        return
    text = "⏯ <b>Antrian:</b>\n"
    for idx, song in enumerate(queue, 1):
        text += f"{idx}. <b>{song['title']}</b> — <i>{song.get('uploader','')}</i>\n"
    await update.message.reply_text(text, parse_mode="HTML")

async def skip_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    next_song = await skip_song(chat_id)
    if next_song:
        await update.message.reply_text(f"⏭️ Lewat! Sekarang memutar: <b>{next_song['title']}</b>", parse_mode="HTML")
    else:
        await update.message.reply_text("Antrian habis.")

async def clear_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    await clear_all_queue(chat_id)
    await update.message.reply_text("🗑️ Antrian dikosongkan.")

async def nowplaying_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    song = await now_playing(chat_id)
    if song:
        await update.message.reply_text(f"🎶 Sekarang diputar: <b>{song['title']}</b>\n{song.get('webpage_url','')}", parse_mode="HTML")
    else:
        await update.message.reply_text("Tidak ada lagu yang sedang diputar.")

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("play", play_command))
    dispatcher.add_handler(CommandHandler("queue", queue_command))
    dispatcher.add_handler(CommandHandler("skip", skip_command))
    dispatcher.add_handler(CommandHandler("clear", clear_command))
    dispatcher.add_handler(CommandHandler("nowplaying", nowplaying_command))