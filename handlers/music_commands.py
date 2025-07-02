from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    CommandHandler,
    CallbackContext,
    MessageHandler,
    filters,
    ConversationHandler,
)
from maestrobot.media.downloader import download_audio, get_lyrics
from maestrobot.player.player_manager import (
    add_to_queue,
    get_now_playing,
    pause,
    resume,
    skip,
    stop,
    set_volume,
    get_global_status,
)
from maestrobot.db.queues import get_queue, clear_queue
import logging

# Helper: Format duration seconds to mm:ss
def format_duration(seconds):
    mins, secs = divmod(int(seconds), 60)
    return f"{mins:02}:{secs:02}"

async def play_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    query = " ".join(context.args)
    if not query:
        await update.message.reply_text("Ketik judul atau link lagu setelah /play")
        return
    msg = await update.message.reply_text("🔎 Sedang mencari lagu...")
    try:
        song = await download_audio(query)
        await add_to_queue(chat_id, song)
        await msg.edit_text(
            f"🎶 <b>Ditambahkan ke antrian:</b> <code>{song['title']}</code>",
            parse_mode="HTML"
        )
    except Exception as e:
        logging.exception(e)
        await msg.edit_text("❌ Gagal memutar lagu.")

async def queue_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    q = await get_queue(chat_id)
    if not q:
        await update.message.reply_text("🎵 Tidak ada lagu dalam antrian.")
        return
    text = "🎶 <b>Antrian Lagu:</b>\n"
    for idx, song in enumerate(q, 1):
        text += f"{idx}. <code>{song['title']}</code> [{format_duration(song['duration'])}]\n"
    await update.message.reply_text(text, parse_mode="HTML")

async def nowplaying_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    song = await get_now_playing(chat_id)
    if not song:
        await update.message.reply_text("🔇 Tidak ada lagu yang sedang diputar.")
        return
    text = (
        f"🎧 <b>Sedang diputar:</b>\n"
        f"Judul: <code>{song['title']}</code>\n"
        f"Durasi: {format_duration(song['duration'])}\n"
        f"Oleh: {song['uploader']}\n"
        f"<a href='{song['source']}'>🌐 Source</a>"
    )
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⏸️ Pause", callback_data="pause"),
            InlineKeyboardButton("▶️ Resume", callback_data="resume"),
            InlineKeyboardButton("⏭️ Skip", callback_data="skip"),
            InlineKeyboardButton("⏹️ Stop", callback_data="stop"),
        ],
        [
            InlineKeyboardButton("📜 Lyrics", callback_data="lyrics"),
        ]
    ])
    await update.message.reply_photo(
        photo=song["thumb"],
        caption=text,
        parse_mode="HTML",
        reply_markup=keyboard
    )

async def pause_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    await pause(chat_id)
    await update.message.reply_text("⏸️ Lagu dijeda.")

async def resume_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    await resume(chat_id)
    await update.message.reply_text("▶️ Pemutaran dilanjutkan.")

async def skip_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    await skip(chat_id)
    await update.message.reply_text("⏭️ Lagu berikutnya.")

async def stop_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    await stop(chat_id)
    await clear_queue(chat_id)
    await update.message.reply_text("⏹️ Pemutaran dihentikan dan antrian dikosongkan.")

async def lyrics_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    song = await get_now_playing(chat_id)
    if not song:
        await update.message.reply_text("Tidak ada lagu yang sedang diputar.")
        return
    # Guess artist from uploader if possible
    artist = song.get("uploader") or None
    lyrics = await get_lyrics(song["title"], artist)
    if lyrics:
        await update.message.reply_text(f"📜 <b>Lirik:</b>\n\n<pre>{lyrics}</pre>", parse_mode="HTML")
    else:
        await update.message.reply_text("❌ Lirik tidak ditemukan.")

async def volume_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Contoh: /volume 100")
        return
    vol = int(context.args[0])
    if not (0 <= vol <= 200):
        await update.message.reply_text("Volume harus di antara 0 - 200.")
        return
    await set_volume(chat_id, vol)
    await update.message.reply_text(f"🔊 Volume diatur ke {vol}.")

async def status_command(update: Update, context: CallbackContext):
    status = await get_global_status()
    await update.message.reply_text(f"📊 <b>Status Player:</b>\n\n{status}", parse_mode="HTML")

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("play", play_command))
    dispatcher.add_handler(CommandHandler("queue", queue_command))
    dispatcher.add_handler(CommandHandler("nowplaying", nowplaying_command))
    dispatcher.add_handler(CommandHandler("pause", pause_command))
    dispatcher.add_handler(CommandHandler("resume", resume_command))
    dispatcher.add_handler(CommandHandler("skip", skip_command))
    dispatcher.add_handler(CommandHandler("stop", stop_command))
    dispatcher.add_handler(CommandHandler("lyrics", lyrics_command))
    dispatcher.add_handler(CommandHandler("volume", volume_command))
    dispatcher.add_handler(CommandHandler("status", status_command))