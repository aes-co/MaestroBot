import os
from pyrogram import Client
from maestrobot.configs import API_ID, API_HASH

async def get_userbot_clients():
    # For now, just one assistant (expandable)
    session_string = os.getenv("USERBOT_SESSION")
    if not session_string:
        raise RuntimeError("USERBOT_SESSION is required!")
    client = Client(
        name="assistant",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=session_string,
        in_memory=True
    )
    return [client]