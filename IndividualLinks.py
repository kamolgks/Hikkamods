__version__ = (0, 0, 5)
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
# meta banner: https://te.legra.ph/file/b15eed35d5ec0dd3a4716.jpg

# meta developer: @shitmodules

import logging

from .. import loader, utils # type: ignore
from telethon.tl.types import Message

logger = logging.getLogger(__name__)


@loader.tds
class IndividualLinksMod(loader.Module):
    """> Links to individual content in telegram."""

    strings = {
        "name": "IndividualLinks",
        "loading": "<emoji document_id=5292226786229236118>🔄</emoji> <b>Loading...</b>",
        "links": (
            "https://t.me/+pbJv2A-WQD0yNGMy\n"
            "https://t.me/kdn4h\n"
            "https://t.me/+70GsDVKwnN1mMmJi\n"
            "https://t.me/antivanil\n"
            "https://t.me/+FMONDOvtkTUwMGNi\n"
            "https://t.me/netvoyotelo\n"
            "https://t.me/Fckk_the_rules\n"
            "https://t.me/porn_in_a_minute\n"
            "https://t.me/+Uay7cXVOXFtHRmLj\n"
            "https://t.me/TheOfficeBruh\n"
            "https://t.me/ne_tvoya_suka\n" # каналы нашел @texmacros
            "https://t.me/+vAqM7BVWT-VlY2Qy\n"
            "https://t.me/+YzDq9RwWlCc1N2Ey\n"
            "https://t.me/+RfdHbMqqeUdiNDUy\n"
            "https://t.me/+EjMIiaCIDzZlMzA6\n"
            "https://t.me/+DRZurxHB_EVkMjZi\n"
            "https://t.me/+fKnl-36ghaI2MjRl\n"
        ),
    }

    strings_ru = {
        "loading": "<emoji document_id=5292226786229236118>🔄</emoji> <b>Загрузка...</b>",
    }

    @loader.command()
    async def flink(self, message: Message):
        """Just send .flink"""
        await utils.answer(message, self.strings["loading"])
        await utils.answer(message, self.strings["links"])
