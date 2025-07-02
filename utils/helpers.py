from datetime import timedelta

def human_time(seconds: int) -> str:
    """Convert detik ke format waktu yang mudah dibaca."""
    return str(timedelta(seconds=seconds))

def mention_html(user_id, name):
    return f'<a href="tg://user?id={user_id}">{name}</a>'