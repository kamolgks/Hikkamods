__version__ = (0, 0, 1)
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

# meta banner: http://devs.farkhodovme.tk/bannerget/kamolgks/gachigallery.png
# meta developer: @shitmodules

import random

from .. import loader
from telethon.tl.types import Message

photos = [
    {"photo": "https://ibb.co/GVcfq7K"},
    {"photo": "https://ibb.co/DQgnfL3"},
    {"photo": "https://ibb.co/FhHsffW"},
    {"photo": "https://ibb.co/NTyw41q"},
    {"photo": "https://ibb.co/gJTQtTf"},
    {"photo": "https://ibb.co/2F5XwtT"},
    {"photo": "https://ibb.co/GHLqjxt"},
    {"photo": "https://ibb.co/frMxckH"},
    {"photo": "https://ibb.co/QD9Pghr"},
    {"photo": "https://ibb.co/GHLqjxt"},
    {"photo": "https://ibb.co/c3T75J3"},
    {"photo": "https://ibb.co/dgMGpj6"},
    {"photo": "https://ibb.co/0G9sQg2"},
    {"photo": "https://ibb.co/FVKJQGp"},
    {"photo": "https://i.imgur.com/5ugBW8K.jpeg"},
    {"photo": "https://i.imgur.com/QJoFN4y.jpeg"},
    {"photo": "https://imgur.io/Z4uZZHx?r"},
]


async def random_photo() -> str:
    sex = random.choice(photos)
    return sex["photo"]


@loader.tds
class GachiGalleryMod(loader.Module):
    """random gachimuchi photos and memes"""

    strings = {"name": "GachiGallery"}

    @loader.command(ru_doc="Скидывает инлайн галерею с мемами (гачи мемы)")
    async def gachicmd(self, message: Message):
        """.gachi > sends random gachi photos and memes"""
        await self.inline.gallery(message, random_photo)
