from maestrobot.db.queues import get_queue, add_to_queue

async def shuffle_queue(chat_id: int):
    queue = await get_queue(chat_id)
    import random
    random.shuffle(queue)
    await add_to_queue(chat_id, queue)