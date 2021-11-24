from userbot.utils import admin_cmd
from . import *
plugin_category = "queen"

@catub.cat_cmd(
    pattern="classy$",
    command=("classy", plugin_category),
    info={
        "header": "To save any destructive pic",
        "usage": [
            "{tr}classy",
        ],
    },
)
async def hello_users(event):
    if event.fwd_from:
        return
    await event.edit("🌹i🥀love💠🌺you⚕️ 🌹i🥀love💠🌺you⚕️ 🌹i🥀love💠🌺you⚕️ 🌹i🥀love💠🌺you⚕️ 🌹i🥀love💠🌺you⚕️ 🌹i🥀love💠🌺you⚕️ 🌹i🥀love💠🌺you⚕️ 🌹i🥀love💠🌺you⚕️ 🌹i🥀love💠🌺you⚕️ 🌹i🥀love💠🌺you⚕️ 🌹i🥀love💠🌺you⚕️ 🌹i🥀love💠🌺you⚕️  🌹.       🍁🍂🎋🌷🌹💐🌸🌼")