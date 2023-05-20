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

# meta pic: https://github.com/kamolgks/assets/raw/main/BotsDeleter.png

# meta developer: @shitmodules

import logging
from .. import loader, utils

from telethon import functions
from telethon.tl.types import Message

logger = logging.getLogger(__name__)


@loader.tds
class BotsDeleterMod(loader.Module):
    """Instant stop or removal of all running Telegram bots"""

    strings = {
        "name": "BotsDeleter",
        "processing": "<emoji document_id=5213452215527677338>⏳</emoji><b>I'm starting to stop the bots ...</b>",
        "assist": "<emoji document_id=5213452215527677338>⏳</emoji><b>I'm starting to remove all bots from the account...</b>",
        "stop": "<emoji document_id=5418063924933173277>👨‍💻</emoji><b>All bots have been successfully stopped</b>",
        "del": "<emoji document_id=5418063924933173277>👨‍💻</emoji><b>All bots have been successfully removed</b>",
    }

    strings_ru = {
        "processing": "<emoji document_id=5213452215527677338>⏳</emoji><b>Начинаю стопать ботов...</b>",
        "assist": "<emoji document_id=5213452215527677338>⏳</emoji><b>Начинаю удаление всех ботов с аккаунта...</b>",
        "stop": "<emoji document_id=5418063924933173277>👨‍💻</emoji><b>Все боты были успешно остановлены</b>",
        "del": "<emoji document_id=5418063924933173277>👨‍💻</emoji><b>Все боты были успешно удалены</b>",
    }

    @loader.command(ru_doc="> Чтобы остановить работу всех ботов")
    async def stopallbotscmd(self, message: Message):
        """> To stop all bots from working"""
        msg = await utils.answer(message, self.strings("processing"))
        t = self.strings("stop")
        k = ""
        async for dialog in self.client.iter_dialogs():
            if hasattr(dialog.entity, "bot"):
                if dialog.entity.bot == True:
                    k += "@" + dialog.entity.username + \
                        "has ID" + str(dialog.id) + "\n"
                    await self.client(functions.contacts.BlockRequest(id=dialog.id))

        await msg.edit(f"{t}")

    @loader.command(ru_doc="> Чтобы удалить диалоги со всеми ботами")
    async def delallbotscmd(self, message: Message):
        """> To delete dialogs with all bots"""
        msg = await utils.answer(message, self.strings("assist"))
        t = self.strings("del")
        k = ""
        async for dialog in self.client.iter_dialogs():
            if hasattr(dialog.entity, "bot"):
                if dialog.entity.bot == True:
                    k += "@" + dialog.entity.username + \
                        "has ID" + str(dialog.id) + "\n"
                    await dialog.delete()

        await msg.edit(f"{t}")
