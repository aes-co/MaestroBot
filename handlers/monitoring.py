import time, platform, psutil, asyncio
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from maestrobot.configs import OWNER_ID, SUDO_USERS
from maestrobot.player import player_manager

def is_sudo_or_owner(user_id):
    return str(user_id) == str(OWNER_ID) or user_id in SUDO_USERS

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start = time.time()
    msg = await update.message.reply_text("🏓 Pong...")
    end = time.time()
    await msg.edit_text(f"🏓 Pong! `{round((end-start)*1000)} ms`", parse_mode="Markdown")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Info sistem singkat
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    uptime = int(time.time() - psutil.boot_time())
    hours, rem = divmod(uptime, 3600)
    minutes, seconds = divmod(rem, 60)
    sysinfo = (
        f"💻 <b>Status Sistem</b>\n"
        f"• CPU: {cpu}%\n"
        f"• RAM: {ram}%\n"
        f"• Uptime: {hours}h {minutes}m {seconds}s\n"
        f"• OS: {platform.system()} {platform.release()}\n"
    )
    # Status player (opsional, jika ada)
    if hasattr(player_manager, "get_global_status"):
        player = await player_manager.get_global_status()
        sysinfo += f"\n🎵 <b>Status Player</b>\n{player}\n"
    await update.message.reply_text(sysinfo, parse_mode="HTML")

async def restart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not is_sudo_or_owner(user.id):
        await update.message.reply_text("🚫 Hanya owner/sudo yang bisa restart bot!")
        return
    await update.message.reply_text("♻️ Bot akan restart sekarang... Bye!")
    await asyncio.sleep(2)
    # Cara restart tergantung deployment, contoh:
    import os, sys
    os.execv(sys.executable, ["python"] + sys.argv)

def register(app):
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("restart", restart))