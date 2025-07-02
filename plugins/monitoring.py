import time
import platform
import psutil
import asyncio

from datetime import datetime
from maestrobot.player import active_calls
from maestrobot.db.queues import get_all_queues

start_time = time.time()

def get_uptime() -> str:
    now = time.time()
    seconds = int(now - start_time)
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return f"{days}d {hours}h {minutes}m {sec}s"

async def get_bot_status() -> str:
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    uptime = get_uptime()

    queues = await get_all_queues()
    total_queues = sum(len(q) for q in queues.values())
    total_chats = len(queues)

    vc_active = len(active_calls)

    python_version = platform.python_version()
    os_info = platform.system() + " " + platform.release()

    text = (
        f"🖥 <b>Status MaestroBot</b>\n\n"
        f"⏱ Uptime: <code>{uptime}</code>\n"
        f"💾 RAM: <code>{ram}%</code>\n"
        f"⚙️ CPU: <code>{cpu}%</code>\n\n"
        f"🎧 VC Aktif: <code>{vc_active}</code>\n"
        f"📂 Queue Aktif: <code>{total_chats}</code>\n"
        f"🎵 Total Lagu Dalam Queue: <code>{total_queues}</code>\n\n"
        f"🐍 Python: <code>{python_version}</code>\n"
        f"🧩 OS: <code>{os_info}</code>"
    )
    return text
