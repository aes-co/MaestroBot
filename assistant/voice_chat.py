from assistant.client import userbot

try:
    from pytgcalls import PyTgCalls
    voice = PyTgCalls(userbot) if userbot else None
except ImportError:
    voice = None