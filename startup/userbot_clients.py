from pyrogram import Client
from maestrobot.assistant.client import get_userbot_clients

async def start_pyrogram_assistants():
    clients = await get_userbot_clients()
    for client in clients:
        await client.start()
    print("All userbot clients started!")