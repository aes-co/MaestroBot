from pyrogram import Client, filters
from pyrogram.types import Message
from maestrobot.configs import OWNER_ID

import time
import platform
import psutil
from maestrobot.player import active_calls
from maestrobot.db.queues import get_all_queues

start_time = time.time()

def get_uptime() -> str:
    seconds = int(time.time() - start_time)
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

    return (
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

@Client.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping_handler(client: Client, message: Message):
    await message.reply("🏓 Pong!")

@Client.on_message(filters.command("restart", prefixes=".") & filters.user(int(OWNER_ID)))
async def restart_handler(client: Client, message: Message):
    await message.reply("♻️ Restarting...")
    import os, sys
    os.execv(sys.executable, [sys.executable] + sys.argv)

@Client.on_message(filters.command("status", prefixes=".") & filters.user(int(OWNER_ID)))
async def status_handler(client: Client, message: Message):
    status = await get_bot_status()
    await message.reply_text(status, parse_mode="html")
