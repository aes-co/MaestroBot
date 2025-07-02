from assistant.client import userbot

async def start_userbot():
    if userbot:
        await userbot.start()
        print("Userbot started")

async def stop_userbot():
    if userbot:
        await userbot.stop()
        print("Userbot stopped")