__version__ = (1, 0, 2)
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
# scope: hikka_min 1.5.3

# meta banner: https://raw.githubusercontent.com/kamolgks/assets/main/AnecdoteGenerator.jpg

# meta developer: @shitmodules


import logging
import random

import aiohttp
from hikkatl.types import Message  # type: ignore

from .. import loader, utils  # type: ignore

chat = "anertsy"

logger = logging.getLogger(__name__)


@loader.tds
class AnecdoteGeneratorMod(loader.Module):
    """Anecdote generator by @shitmodules"""

    strings = {
        "name": "AnecdoteGenerator",
        "loading": "<emoji document_id=5451732530048802485>⏳</emoji> Loading...",
        "error": "<emoji document_id=5197593315075169671>😢</emoji> Something went wrong, try again",
    }

    strings_ru = {
        "loading": "<emoji document_id=5451732530048802485>⏳</emoji> Загрузка...",
        "error": "<emoji document_id=5197593315075169671>😢</emoji> Что-то пошло не так, попробуй снова",
    }

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.messages = await self.client.get_messages(chat, limit=None)

    @loader.command(ru_doc="Генерирует анекдоты (они не всегда смешные)")
    async def anec(self, message: Message):
        """Sends an anecdote (not always funny)"""
        wtf = random.choice(self.messages)
        await utils.answer(message, wtf)

    @loader.command()
    async def joke(self, message: Message):
        """Sends an anecdote x2 (not always funny)"""
        try:
            await utils.answer(message, self.strings["loading"])
            url = "https://v2.jokeapi.dev/joke/Any"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    response.raise_for_status()
                    data = await response.json()
                    if data:
                        joke = data.get("joke")
                        answer_text = joke if joke else self.strings["error"]
                    else:
                        answer_text = self.strings["error"]

            await utils.answer(message, answer_text)

        except aiohttp.ClientError as e:
            await utils.answer(message, f"<i>{e}</i>")
