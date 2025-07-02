from telegram.ext import Application
from maestrobot.configs import BOT_TOKEN
from maestrobot.handlers import (
    start_help,
    music_commands,
    admin_commands,
    settings_commands,
    utility_commands
)

async def start_ptb_bot():
    app = Application.builder().token(BOT_TOKEN).build()
    start_help.register(app)
    music_commands.register(app)
    admin_commands.register(app)
    settings_commands.register(app)
    utility_commands.register(app)
    print("PTB bot started!")
    await app.run_polling()