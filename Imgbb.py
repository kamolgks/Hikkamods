__version__ = (1, 0, 0)
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
from telethon.tl.types import Message

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class ImgbbMod(loader.Module):
    """Upload media to imgbb.com"""

    strings = {
        "name": "Imgbb",
        "api_key_doc": "API key for imgbb",
        "no_api_key": "<b><u>API key</u> is not specified, it can be obtained on the website imgbb.com/api and then enter it into the module config: <code>.config Imgbb</code></b>",
        "no_reply": "<b>The file reply was not found.</b>",
        "error": "<b>Failed to upload</b>",
    }

    strings_ru = {
        "api_key_doc": "API-ключ для imgbb",
        "no_api_key": "<b><u>Ключ API</u> не найден, его можно получить на сайте imgbb.com/api и затем ввести в конфиг модуля: <code>.config Imgbb</code></b>",
        "no_reply": "<b>Не найден реплай на файл.</b>",
        "error": "<b>Не удалось загрузить</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "api_key",
                None,
                lambda: self.strings["api_key_doc"],
                validator=loader.validators.Hidden(loader.validators.String()),
            ),
        )

    @loader.command(ru_doc=".imgbb <файл> - загрузить файл на imgbb.com")
    async def imgbb(self, message: Message):
        """.imgbb <file> - upload file to imgbb.com"""
        try:
            reply = await message.get_reply_message()
            if not reply or not reply.file:
                return await utils.answer(message, self.strings("no_reply"))
        
            api_key = self.config["api_key"]
            if not api_key:
                return await utils.answer(message, self.strings("no_api_key"))
        
            file = io.BytesIO(await reply.download_media(bytes))
            response = requests.post("https://api.imgbb.com/1/upload", data={"key": self.config["api_key"]}, files={"image": file})
            
            if response.status_code != 200:
                return await utils.answer(message, self.strings("error"))
            
            response = response.json()["data"]
            url = response["url_viewer"]
            await utils.answer(message, f'<b>🪄Your file <a href="{url}">uploaded</a> - <code>{response["url"]}</code>')
            logging.info("ImgbbMod: Your file has been uploaded successfully")
        
        except Exception as e:
            await utils.answer(message, "<b>Failed to upload: <u>{}</u><b>".format(e))
