import logging
from telegram.ext import Application, ContextTypes
from maestrobot.configs import OWNER_ID, SUDO_USERS

# Import semua modul setup
from maestrobot.handlers import settings_commands, admin_commands
from maestrobot.player import player_manager
from maestrobot.plugins import (
    lyrics,
    recommendations,
    shared_queue,
    playlist,
)

def main():
    import os
    TOKEN = os.environ.get("BOT_TOKEN")
    if not TOKEN:
        raise Exception("BOT_TOKEN env var not set")
    logging.basicConfig(level=logging.INFO)
    app = Application.builder().token(TOKEN).build()

    # Register command handlers
    settings_commands.setup(app)
    admin_commands.setup(app)
    player_manager.setup(app)
    lyrics.setup(app)
    recommendations.setup(app)
    shared_queue.setup(app)
    playlist.setup(app)

    print("Bot started!")
    app.run_polling()

if __name__ == "__main__":
    main()