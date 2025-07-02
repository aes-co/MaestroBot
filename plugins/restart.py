from telegram.ext import CommandHandler
import os, sys

async def restart_command(update, context):
    await update.message.reply_text("Restarting...")
    os.execv(sys.executable, ["python"] + sys.argv)

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("restart", restart_command))