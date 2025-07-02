import time
import platform
import psutil
import asyncio
import os
import sys
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from maestrobot.configs import OWNER_ID, SUDO_USERS
from maestrobot.player import player_manager


def is_sudo_or_owner(user_id):
    return str(user_id) == str(OWNER_ID) or user_id in SUDO_USERS


async def ping_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start = time.time()
    msg = await update.message.reply_text("🏓 Pong...")
    end = time.time()
    await msg.edit_text(f"🏓 Pong! `{round((end - start) * 1000)} ms`", parse_mode="Markdown")


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    uptime = int(time.time() - psutil.boot_time())
    hours, rem = divmod(uptime, 3600)
    minutes, seconds = divmod(rem, 60)
    text = (
        f"💻 <b>Status Sistem</b>\n"
        f"• CPU: {cpu}%\n"
        f"• RAM: {ram}%\n"
        f"• Uptime: {hours}h {minutes}m {seconds}s\n"
        f"• OS: {platform.system()} {platform.release()}\n"
    )
    if hasattr(player_manager, "get_global_status"):
        status = await player_manager.get_global_status()
        text += f"\n🎵 <b>Status Player</b>\n{status}\n"
    await update.message.reply_text(text, parse_mode="HTML")


async def restart_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not is_sudo_or_owner(user_id):
        await update.message.reply_text("🚫 Hanya owner/sudo yang bisa restart bot!")
        return
    await update.message.reply_text("♻️ Bot akan restart sekarang... Bye!")
    await asyncio.sleep(2)
    os.execv(sys.executable, [sys.executable] + sys.argv)


handlers = [
    CommandHandler("ping", ping_command),
    CommandHandler("status", status_command),
    CommandHandler("restart", restart_command),
]
