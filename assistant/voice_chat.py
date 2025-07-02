from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputStream, AudioPiped
from pytgcalls.types.stream import StreamAudioEnded
from pyrogram import Client
from typing import Dict, Optional
from maestrobot.clients import userbot

class VoiceCallManager:
    def __init__(self):
        self.clients: Dict[int, PyTgCalls] = {}
        self.streams: Dict[int, str] = {}

    def get_client(self, chat_id: int) -> PyTgCalls:
        if chat_id not in self.clients:
            tgcall = PyTgCalls(userbot)
            tgcall.on_stream_end()(self._on_stream_end)
            self.clients[chat_id] = tgcall
        return self.clients[chat_id]

    async def join_voice(self, chat_id: int, file_path: str):
        client = self.get_client(chat_id)
        if not client._client.is_connected:
            await client.start()
        input_stream = InputStream(AudioPiped(file_path))
        await client.join_group_call(chat_id, input_stream)
        self.streams[chat_id] = file_path

    async def leave_voice(self, chat_id: int):
        client = self.get_client(chat_id)
        await client.leave_group_call(chat_id)
        if chat_id in self.streams:
            del self.streams[chat_id]

    async def stop_stream(self, chat_id: int):
        client = self.get_client(chat_id)
        await client.stop_stream(chat_id)
        if chat_id in self.streams:
            del self.streams[chat_id]

    async def _on_stream_end(self, client: PyTgCalls, update: Update):
        if isinstance(update, StreamAudioEnded):
            chat_id = update.chat_id
            if chat_id in self.streams:
                del self.streams[chat_id]

vc_manager = VoiceCallManager()
