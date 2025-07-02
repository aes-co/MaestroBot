from telegram.ext import MessageFilter
from maestrobot.configs import OWNER_ID

class IsOwnerFilter(MessageFilter):
    def filter(self, message):
        return message.from_user and message.from_user.id == int(OWNER_ID)

is_owner = IsOwnerFilter()
