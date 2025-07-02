from telegram import Update
from telegram.ext import CallbackContext, CallbackQueryHandler
from maestrobot.player.player_manager import pause, resume, skip, stop, get_now_playing
from maestrobot.media.downloader import get_lyrics

async def control_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    chat_id = query.message.chat.id

    if data == "pause":
        await pause(chat_id)
        await query.answer("⏸️ Dijeda")
    elif data == "resume":
        await resume(chat_id)
        await query.answer("▶️ Dilanjutkan")
    elif data == "skip":
        await skip(chat_id)
        await query.answer("⏭️ Berikutnya")
    elif data == "stop":
        await stop(chat_id)
        await query.answer("⏹️ Dihentikan")
    elif data == "lyrics":
        song = await get_now_playing(chat_id)
        artist = song.get("uploader") if song else None
        title = song.get("title") if song else None
        if song and title:
            lyrics = await get_lyrics(title, artist)
            if lyrics:
                await query.message.reply_text(f"📜 <b>Lirik:</b>\n\n<pre>{lyrics}</pre>", parse_mode="HTML")
            else:
                await query.message.reply_text("❌ Lirik tidak ditemukan.")
        else:
            await query.message.reply_text("Tidak ada lagu yang sedang diputar.")
        await query.answer("")

def setup(dispatcher):
    dispatcher.add_handler(CallbackQueryHandler(
        control_callback,
        pattern="^(pause|resume|skip|stop|lyrics)$"
    ))  