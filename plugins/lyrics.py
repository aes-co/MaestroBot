import aiohttp
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

LYRICS_API_URL = "https://some-lyrics-api.com/lyrics"  # Ganti dengan endpoint API lirik yang kamu pakai

async def fetch_lyrics(query: str):
    """
    Ambil lirik lagu dari API eksternal.
    """
    params = {"q": query}
    async with aiohttp.ClientSession() as session:
        async with session.get(LYRICS_API_URL, params=params) as resp:
            if resp.status != 200:
                return None
            data = await resp.json()
            return data.get("lyrics")

async def lyrics_command(update: Update, context: CallbackContext):
    if not context.args:
        await update.message.reply_text("Kirim: /lyrics <judul/penyanyi>")
        return
    query = " ".join(context.args)
    lyrics = await fetch_lyrics(query)
    if not lyrics:
        await update.message.reply_text("Lirik tidak ditemukan, coba judul/artis lain.")
        return
    # Telegram membatasi 4096 karakter per pesan
    MAX_LEN = 4000
    text = f"<b>Lirik '{query}':</b>\n\n{lyrics}"
    for i in range(0, len(text), MAX_LEN):
        await update.message.reply_text(text[i:i+MAX_LEN], parse_mode="HTML")

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("lyrics", lyrics_command))