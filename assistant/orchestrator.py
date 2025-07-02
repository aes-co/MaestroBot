import asyncio
from maestrobot.assistant.client import client
from maestrobot.startup.bot_client import app as bot
from maestrobot.handlers import (
    start_help,
    music_commands,
    admin_commands,
    settings_commands,
    utility_commands,
    monitoring,
)
from maestrobot.plugins import (
    restart,
    lyrics,
    music_controls,
    shared_queue,
    recommendations,
    moderation_vc,
    monitoring as plugin_monitoring
)
from maestrobot.startup.db_connections import init_db_connections


def load_handlers():
    bot.add_handlers(start_help.handlers)
    bot.add_handlers(music_commands.handlers)
    bot.add_handlers(admin_commands.handlers)
    bot.add_handlers(settings_commands.handlers)
    bot.add_handlers(utility_commands.handlers)
    bot.add_handlers(monitoring.handlers)


def load_plugins():
    bot.add_handlers(restart.handlers)
    bot.add_handlers(lyrics.handlers)
    bot.add_handlers(music_controls.handlers)
    bot.add_handlers(shared_queue.handlers)
    bot.add_handlers(recommendations.handlers)
    bot.add_handlers(moderation_vc.handlers)
    bot.add_handlers(plugin_monitoring.handlers)


async def start():
    await init_db_connections()
    load_handlers()
    load_plugins()
    await bot.initialize()
    await client.start()
    await bot.start()
    print("MaestroBot started.")
    await asyncio.get_event_loop().create_future()


if __name__ == "__main__":
    asyncio.run(start())
