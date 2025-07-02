from pyrogram import Client
import os

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")

if __name__ == "__main__":
    with Client(":memory:", api_id=API_ID, api_hash=API_HASH) as app:
        print(app.export_session_string())