from collections import defaultdict
from maestrobot.player.voice_chat import join_or_get_group_call, leave_group_call
from maestrobot.player.transcoder import transcode_audio, cleanup_transcoded
from maestrobot.db.queues import get_queue, pop_queue, log_playback
import asyncio

active_players = {}

class Player:
    def __init__(self, chat_id, group_call):
        self.chat_id = chat_id
        self.group_call = group_call
        self.queue = []
        self.now_playing = None
        self.volume = 100
        self.playing = False
        self.task = None

    async def load_queue(self):
        self.queue = await get_queue(self.chat_id)

    async def play_next(self):
        if not self.queue:
            self.playing = False
            await leave_group_call(self.chat_id)
            return
        self.now_playing = await pop_queue(self.chat_id)
        audio_path = await transcode_audio(self.now_playing["id"], self.chat_id)
        if not audio_path:
            return await self.play_next()
        await self.group_call.start_playout(audio_path)
        self.playing = True
        await log_playback(self.chat_id, self.now_playing)

    async def start(self):
        if self.playing:
            return
        await self.load_queue()
        if not self.queue:
            return
        await self.play_next()

    async def skip(self):
        await self.group_call.stop_playout()
        await self.play_next()

    async def stop(self):
        await self.group_call.stop_playout()
        self.queue = []
        self.now_playing = None
        self.playing = False
        await leave_group_call(self.chat_id)
        cleanup_transcoded(self.chat_id)

    async def pause(self):
        await self.group_call.pause_playout()

    async def resume(self):
        await self.group_call.resume_playout()

    async def set_volume(self, vol):
        self.volume = vol
        await self.group_call.set_volume(vol)

async def get_player(chat_id: int):
    if chat_id in active_players:
        return active_players[chat_id]
    group_call = await join_or_get_group_call(chat_id)
    player = Player(chat_id, group_call)
    active_players[chat_id] = player
    return player

async def add_to_queue(chat_id: int, song: dict):
    player = await get_player(chat_id)
    player.queue.append(song)
    if not player.playing:
        await player.start()

async def get_now_playing(chat_id: int):
    player = active_players.get(chat_id)
    return player.now_playing if player else None

async def pause(chat_id: int):
    player = active_players.get(chat_id)
    if player:
        await player.pause()

async def resume(chat_id: int):
    player = active_players.get(chat_id)
    if player:
        await player.resume()

async def skip(chat_id: int):
    player = active_players.get(chat_id)
    if player:
        await player.skip()

async def stop(chat_id: int):
    player = active_players.get(chat_id)
    if player:
        await player.stop()
        active_players.pop(chat_id, None)

async def set_volume(chat_id: int, vol: int):
    player = active_players.get(chat_id)
    if player:
        await player.set_volume(vol)

async def get_global_status():
    text = ""
    for chat_id, player in active_players.items():
        if player.now_playing:
            title = player.now_playing["title"]
            text += f"\n<b>{chat_id}</b>: 🎶 {title}"
    return text or "Tidak ada pemutaran aktif."

async def mute_voice_chat(chat_id: int):
    player = active_players.get(chat_id)
    if player:
        await player.group_call.set_is_muted(True)

async def unmute_voice_chat(chat_id: int):
    player = active_players.get(chat_id)
    if player:
        await player.group_call.set_is_muted(False)

async def kick_from_voice_chat(chat_id: int, user_id: int):
    player = active_players.get(chat_id)
    if player:
        await player.group_call.kick_user(user_id)
