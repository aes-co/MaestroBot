import re
import aiohttp
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

GENIUS_SEARCH_URL = "https://genius.com/api/search/multi"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

async def fetch_lyrics(query: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(GENIUS_SEARCH_URL, params={"q": query}, headers=HEADERS) as resp:
            if resp.status != 200:
                return None
            data = await resp.json()
            sections = data["response"]["sections"]
            for section in sections:
                if section["type"] == "song":
                    hits = section["hits"]
                    if hits:
                        url = hits[0]["result"]["url"]
                        return await scrape_lyrics(url, session)
    return None

async def scrape_lyrics(url: str, session: aiohttp.ClientSession) -> str:
    async with session.get(url, headers=HEADERS) as resp:
        html = await resp.text()
        soup = BeautifulSoup(html, "html.parser")
        lyrics_divs = soup.select("div[data-lyrics-container=true]")
        if not lyrics_divs:
            return "Lirik tidak ditemukan."
        lyrics = "\n".join(div.get_text(separator="\n").strip() for div in lyrics_divs)
        return re.sub(r"\n{3,}", "\n\n", lyrics).strip()

async def lyrics_command(update: Update, context: CallbackContext):
    if not context.args:
        await update.message.reply_text("Kirim: /lyrics <judul/penyanyi>")
        return
    query = " ".join(context.args)
    lyrics = await fetch_lyrics(query)
    if not lyrics:
        await update.message.reply_text("Lirik tidak ditemukan, coba judul/artis lain.")
        return
    MAX_LEN = 4000
    for i in range(0, len(lyrics), MAX_LEN):
        await update.message.reply_text(lyrics[i:i+MAX_LEN], parse_mode="HTML")

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("lyrics", lyrics_command))
