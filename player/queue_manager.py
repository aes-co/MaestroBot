from collections import defaultdict
from maestrobot.player.player import Player
from maestrobot.db.playback_history import log_playback

await log_playback(message.from_user.id, track)

class QueueManager:
    def __init__(self):
        self.players = defaultdict(Player)

    def get_player(self, chat_id: int) -> Player:
        return self.players[chat_id]

    def remove_player(self, chat_id: int):
        if chat_id in self.players:
            del self.players[chat_id]

queue_manager = QueueManager()
