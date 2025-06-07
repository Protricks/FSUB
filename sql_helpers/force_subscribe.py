# force_subscribe.py

from mongo_helpers import force_subscribe_collection

async def fs_settings(chat_id: int):
    """
    Get the force subscribe setting for a specific chat.
    """
    return await force_subscribe_collection.find_one({"chat_id": chat_id})


async def add_channel(chat_id: int, channel: str):
    """
    Add or update a force subscribe setting.
    """
    await force_subscribe_collection.update_one(
        {"chat_id": chat_id},
        {"$set": {"channel": channel}},
        upsert=True
    )


async def disapprove(chat_id: int):
    """
    Remove force subscribe setting for a chat.
    """
    await force_subscribe_collection.delete_one({"chat_id": chat_id})
