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
# scope: hikka_min 1.6.3

# meta pic: https://x0.at/TPOM.png
# meta banner:

# meta developer: @shitmodules

import logging
import requests

from .. import loader, utils  # type: ignore
from hikkatl.types import Message  # type: ignore

logger = logging.getLogger(__name__)


@loader.tds
class QuoteGen(loader.Module):
    """Generation quote"""

    strings = {
        "name": "QuoteGen",
        "loading": "<emoji document_id=5289930378885214069>✍️</emoji><b>Search for a quote...</b>",
        "result": "<b><blockquote>{}</blockquote>\n\n<emoji document_id=5247213725080890199>©️</emoji><i>{}</i></b>",
        "err": "<b>An error occurred, please try later</b>",
    }

    def __init__(self):
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self._client = client
        self._db = db

    @loader.command()
    async def qn(self, message: Message):
        """Usage: .qn"""
        await utils.answer(message, self.strings["loading"])
        data = (await utils.run_sync(requests.get, "https://api.quotable.io/random")).json()
        if data:
            await utils.answer(message, self.strings["result"].format(data.get("content"), data.get("author")))
        else:
            await utils.answer(message, self.strings["err"])
