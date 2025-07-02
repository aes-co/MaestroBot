import os
from dotenv import load_dotenv

load_dotenv()

def get_env(name, default=None, required=True, cast=str):
    value = os.getenv(name, default)
    if required and value is None:
        raise RuntimeError(f"Missing required environment variable: {name}")
    if value is not None and cast:
        try:
            if cast == bool:
                value = value.lower() in ("1", "true", "yes", "on")
            else:
                value = cast(value)
        except Exception as e:
            raise RuntimeError(f"Could not cast {name}: {e}")
    return value

API_ID = get_env("API_ID", cast=int)
API_HASH = get_env("API_HASH")
BOT_TOKEN = get_env("BOT_TOKEN")
BOT_USERNAME = get_env("BOT_USERNAME")
OWNER_ID = get_env("OWNER_ID", cast=int)
SUDO_USERS = [int(x) for x in os.getenv("SUDO_USERS", "").split() if x.strip()]
MONGO_URI = get_env("MONGO_URI")
REDIS_URI = get_env("REDIS_URI")
RABBITMQ_URI = os.getenv("RABBITMQ_URI")
KAFKA_URI = os.getenv("KAFKA_URI")
CREATOR_CHANNEL_ID = get_env("CREATOR_CHANNEL_ID", cast=int)
CREATOR_CHANNEL_LINK = get_env("CREATOR_CHANNEL_LINK")
DONATION_LINK = os.getenv("DONATION_LINK")
AUDIO_QUALITY = os.getenv("AUDIO_QUALITY", "high")