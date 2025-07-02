from assistant.client import userbot

if userbot:
    @userbot.on_message()
    async def echo(client, message):
        if message.text == "/ping":
            await message.reply("pong (dari userbot)")