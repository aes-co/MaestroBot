import datetime

def format_duration(seconds: int) -> str:
    """
    Format detik menjadi MM:SS.
    """
    minutes, secs = divmod(int(seconds), 60)
    return f"{minutes:02}:{secs:02}"

def human_readable_size(size: int, decimal_places: int = 2) -> str:
    """
    Ubah bytes ke ukuran manusiawi (KB, MB, GB, dst).
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.{decimal_places}f} {unit}"
        size /= 1024
    return f"{size:.{decimal_places}f} PB"

def get_timestamp() -> str:
    """
    Timestamp sekarang dalam format ISO 8601.
    """
    return datetime.datetime.utcnow().isoformat()

def mention_html(user_id: int, name: str) -> str:
    """
    Mention user dalam format HTML.
    """
    return f'<a href="tg://user?id={user_id}">{name}</a>'
