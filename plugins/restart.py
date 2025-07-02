import os
import sys
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from maestrobot.configs import OWNER_ID

async def restart_command(update: Update, context: CallbackContext):
    if update.effective_user.id != int(OWNER_ID):
        await update.message.reply_text("❌ Kamu tidak diizinkan menggunakan perintah ini.")
        return

    await update.message.reply_text("♻️ Restarting bot...")
    os.execv(sys.executable, [sys.executable] + sys.argv)

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("restart", restart_command))
