from telegram.ext import MessageFilter

class IsOwnerFilter(MessageFilter):
    def __init__(self, owner_id):
        self.owner_id = owner_id

    def filter(self, message):
        return message.from_user.id == self.owner_id

is_owner = IsOwnerFilter