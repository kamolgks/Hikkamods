__version__ = (0, 0, 4)
# *
# *              $$\       $$\   $$\                                   $$\           $$\
# *              $$ |      \__|  $$ |                                  $$ |          $$ |
# *     $$$$$$$\ $$$$$$$\  $$\ $$$$$$\   $$$$$$\$$$$\   $$$$$$\   $$$$$$$ |$$\   $$\ $$ | $$$$$$\   $$$$$$$\
# *    $$  _____|$$  __$$\ $$ |\_$$  _|  $$  _$$  _$$\ $$  __$$\ $$  __$$ |$$ |  $$ |$$ |$$  __$$\ $$  _____|
# *    \$$$$$$\  $$ |  $$ |$$ |  $$ |    $$ / $$ / $$ |$$ /  $$ |$$ /  $$ |$$ |  $$ |$$ |$$$$$$$$ |\$$$$$$\
# *     \____$$\ $$ |  $$ |$$ |  $$ |$$\ $$ | $$ | $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |$$   ____| \____$$\
# *    $$$$$$$  |$$ |  $$ |$$ |  \$$$$  |$$ | $$ | $$ |\$$$$$$  |\$$$$$$$ |\$$$$$$  |$$ |\$$$$$$$\ $$$$$$$  |
# *    \_______/ \__|  \__|\__|   \____/ \__| \__| \__| \______/  \_______| \______/ \__| \_______|\_______/
# *
# *
# *            © Copyright 2023
# *
# *         https://t.me/shitmodules
# *
# 🔒 Code is licensed under CC-BY-NC-ND 4.0 unless otherwise specified.
# 🌐 https://creativecommons.org/licenses/by-nc-nd/4.0/

# You CANNOT edit this file without direct permission from the author.
# You can redistribute this file without any changes.

# scope: hikka_only
# scope: hikka_min 1.6.2

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/IndividualLinks.jpg
# meta banner: https://raw.githubusercontent.com/kamolgks/assets/main/IndividualLinks.jpg

# meta developer: @shitmodules

import logging

from .. import loader, utils
from telethon.tl.types import Message

logger = logging.getLogger(__name__)


@loader.tds
class IndividualLinks(loader.Module):
    """
    Links to individual content in telegram.
    ⛔Do not try to use this module in groups, it only works in PM
    """

    strings = {
        "name": "IndividualLinks",
        "link": (
            "https://t.me/+YJXUGPO--KU2YzBi\n"
            "https://t.me/+b3ThTlaz2AczOTZl\n"
            "https://t.me/+Ve0XZLOgWg8yODdi\n"
            "https://t.me/+yegz2e53-bFmZjIy\n"
            "https://t.me/+RfdHbMqqeUdiNDUy\n"
            "https://t.me/+1Us4Bg6rR3hjZjFl\n"
            "https://t.me/+scyfvcZMh1YyOWIy\n"
            "https://t.me/+EjMIiaCIDzZlMzA6\n"
            "https://t.me/+ISFyMTT7TJJjODNi\n"
            "https://t.me/+DRZurxHB_EVkMjZi\n"
            "https://t.me/+xjQ_Qe3pOtgxODJl\n"
            "https://t.me/+0F355GmUWd4yZDA6\n"
            "https://t.me/+IzGPBgYxa1FhMmEy\n"
            "https://t.me/+t0mw7PpRJks2YTQy\n"
            "https://t.me/+NUwqHxff4DM0NjE9\n"
            "https://t.me/+fKnl-36ghaI2MjRl\n"
            "https://t.me/+xfNMApu2YpA5YmYy\n"
        ),
        "link-2": (
            "https://t.me/+4Cbqczaexc8xMGJi\n"
            "https://t.me/+TfSJi7Xg6SNlZGJi\n"
            "https://t.me/+jJlbvbnMQHJiYzBi\n"
            "https://t.me/+-OsCW3qLfiVjMGVi\n"
            "https://t.me/+HUuBDnMf3utkYTIy\n"
            "https://t.me/+eu8omMCpks1kNjIy\n"
            "https://t.me/+ibZzteZEQ_gwYjIy\n"
        )
    }

    @loader.command()
    async def indcmd(self, message: Message):
        """> Links to individual content in telegram"""
        await utils.answer(
            message,
            self.strings("link"),
        )

    @loader.command()
    async def oopscmd(self, message: Message):
        """> Links to individual content in telegram (photos)"""
        await utils.answer(
            message,
            self.strings("link-2"),
        )
