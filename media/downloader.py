import yt_dlp
import asyncio

# Fungsi utama download audio (untuk queue, playlist, dsb)

YTDL_OPTS = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "noplaylist": True,
    "quiet": True,
    "extract_flat": False,
    "nocheckcertificate": True,
    "cachedir": False,
    "default_search": "ytsearch",
    "source_address": "0.0.0.0",
    "geo_bypass": True,
}

async def download_audio(query: str):
    """
    Download audio dari YouTube/Spotify dan return info lagu.
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _download_audio_sync, query)

def _download_audio_sync(query):
    with yt_dlp.YoutubeDL(YTDL_OPTS) as ydl:
        info = ydl.extract_info(query, download=False)
        # Untuk hasil pencarian, ambil entri pertama
        if "entries" in info:
            info = info["entries"][0]
        return {
            "title": info.get("title"),
            "duration": info.get("duration"),
            "uploader": info.get("uploader") or info.get("channel"),
            "webpage_url": info.get("webpage_url"),
            "thumbnail": info.get("thumbnail"),
            "id": info.get("id"),
            "source": info.get("extractor_key"),
        }