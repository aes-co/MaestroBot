from pyrogram import Client
from maestrobot.assistant.client import get_userbot_clients

userbot_clients: list[Client] = []

async def start_pyrogram_assistants():
    global userbot_clients
    userbot_clients = await get_userbot_clients()
    for client in userbot_clients:
        await client.start()
    print(f"✅ {len(userbot_clients)} userbot client(s) started.")

async def stop_pyrogram_assistants():
    for client in userbot_clients:
        await client.stop()
    print("🛑 All userbot clients stopped.")
