from telegram import Update
from telegram.ext import CallbackContext, CallbackQueryHandler
from maestrobot.player import pause, resume, skip, stop, get_active_track
from maestrobot.media.lyrics import get_lyrics  # fungsi versi baru kamu

async def control_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    chat_id = query.message.chat.id

    if data == "pause":
        await pause(chat_id)
        await query.answer("⏸️ Dipause")
    elif data == "resume":
        await resume(chat_id)
        await query.answer("▶️ Dilanjutkan")
    elif data == "skip":
        await skip(chat_id)
        await query.answer("⏭️ Dilewati")
    elif data == "stop":
        await stop(chat_id)
        await query.answer("⏹️ Dihentikan")
    elif data == "lyrics":
        track = get_active_track(chat_id)
        if not track:
            await query.message.reply_text("❌ Tidak ada lagu yang sedang diputar.")
            await query.answer()
            return

        title = track.get("title")
        artist = track.get("artist")
        lyrics = await get_lyrics(f"{title} {artist or ''}")
        if not lyrics:
            await query.message.reply_text("❌ Lirik tidak ditemukan.")
        else:
            chunks = [lyrics[i:i+4000] for i in range(0, len(lyrics), 4000)]
            for part in chunks:
                await query.message.reply_text(f"<b>Lirik:</b>\n\n<pre>{part}</pre>", parse_mode="HTML")
        await query.answer()

def setup(dispatcher):
    dispatcher.add_handler(CallbackQueryHandler(
        control_callback,
        pattern="^(pause|resume|skip|stop|lyrics)$"
    ))
