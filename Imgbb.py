__version__ = (1, 0, 3)
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

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/Imgbb.jpg
# meta banner: https://raw.githubusercontent.com/kamolgks/assets/main/Imgbb.jpeg

# meta developer: @shitmodules

import io
import logging
import requests

from .. import loader, utils # type: ignore
from hikkatl.types import Message # type: ignore

logger = logging.getLogger(__name__)


@loader.tds
class Imgbb(loader.Module):
    """Upload media to imgbb.com"""

    strings = {
        "name": "Imgbb",
        "_cfg_doc_api": "API key for imgbb",
        "no_api_key": "<b><u>API key</u> is not specified, it can be obtained on the website imgbb.com/api and then enter it into the module config:</b> <code>{}config Imgbb</code>",
        "no_reply": "<b>The file reply was not found.</b>",
        "error": "<b>Failed to upload</b> Try again.",
        "result": "🪄 <b>Your file uploaded</b> - <code>{}</code>",
    }

    strings_ru = {
        "_cfg_doc_api": "API-ключ для imgbb",
        "no_api_key": "<b><u>Ключ API</u> не найден, его можно получить на сайте imgbb.com/api и затем ввести в конфиг модуля:</b> <code>{}config Imgbb</code>",
        "no_reply": "<b>Не найден реплай на файл.</b>",
        "error": "<b>Не удалось загрузить</b> Попробуй ещё раз.",
        "result": "🪄 <b>Твой файл загружен</b> - <code>{}</code>",
    }

    def __init__(self):
        self.name = self.strings["name"]
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "api_key",
                None,
                doc=lambda: self.strings["_cfg_doc_api"],
                validator=loader.validators.Hidden(loader.validators.String()),
            ),
        )

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

    @loader.command(ru_doc=".imgbb <файл> - загрузить файл на imgbb.com")
    async def imgbb(self, message: Message):
        """.imgbb  - upload file to imgbb.com"""
        try:
            api_key = self.config["api_key"]
            if not api_key:
                return await utils.answer(message, self.strings["no_api_key"].format(self.get_prefix()))

            reply = await message.get_reply_message()
            if not reply or not reply.file:
                return await utils.answer(message, self.strings["no_reply"])

            file = io.BytesIO(await reply.download_media(bytes))
            data = (await utils.run_sync(requests.post, "https://api.imgbb.com/1/upload", data={"key": self.config["api_key"]}, files={"image": file})).json()
            if data:
                await utils.answer(message, self.strings["result"].format(data["data"].get("url_viewer", "")))
            else:
                await utils.answer(message, self.stringa["error"])

        except Exception:
            await utils.answer(message, self.strings["error"])
