from asyncio import sleep

from userbot import catub
from userbot.core.logger import logging

plugin_category = "queen"
LOGS = logging.getLogger(__name__)


@catub.cat_cmd(
    pattern="slfchk$",
    command=("slfchk", plugin_category),
    info={
        "header": "To save any destructive pic",
        "usage": [
            "{tr}slfchk",
        ],
    },
)
async def oho(event):
    if not event.is_reply:
        return await event.edit("Reply to a self distructing pic !.!.!")
    k = await event.get_reply_message()
    pic = await k.download_media()
    await catub.send_file(event.chat_id, pic)
    await event.delete()
