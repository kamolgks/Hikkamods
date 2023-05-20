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

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/CDZ-Searcher.jpg
# meta banner: http://devs.farkhodovme.tk/bannerget/kamolgks/cdz-searcher.png

# meta developer: @shitmodules

import logging

from telethon.tl.types import Message
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import utils, loader

logger = logging.getLogger(__name__)


@loader.tds
class CDZSearcherMod(loader.Module):
    """Module for searching for answers from CDZ, you just need to enter a link to the tests."""

    strings = {
        "name": "CDZ-Searcher",
        "processing": (
            "<emoji document_id=5346152548761868765>💜</emoji><b>Processing...</b>"
        ),
        "no_link": (
            "<emoji document_id=5787344491488742956>🎮</emoji><b>Where is the link?</b>"
        ),
        "unl_bot": (
            "<emoji document_id=5785038454828043276>✖️</emoji>Unlock - @CDZ_AnswersBot"
        ),
    }

    strings_ru = {
        "processing": (
            "<emoji document_id=5346152548761868765>💜</emoji><b>Загрузка...</b>"
        ),
        "no_link": (
            "<emoji document_id=5787344491488742956>🎮</emoji><b>А где ссылка?</b>"
        ),
        "unl_bot": (
            "<emoji document_id=5785038454828043276>✖️</emoji>Разблокируй - @CDZ_AnswersBot"
        ),
    }

    @loader.command(
        ru_doc="> Находит ответы из гдз, нужно просто ввести ссылку на тесты.",
    )
    async def cdzcmd(self, message: Message):
        """> Enter a link to the tests"""
        start = "/start"
        link = utils.get_args_raw(message)
        if link == "":
            await utils.answer(message, self.strings("no_link"))
            return

        msg = await utils.answer(message, self.strings("processing"))

        async with self._client.conversation("CDZ_AnswersBot") as conv:
            try:
                bot = []
                bot += [await conv.send_message(start)]
                bot += [await conv.send_message(link)]
                send = await conv.get_response()
            except YouBlockedUserError:
                await utils.answer(message, self.strings("unl_bot"))
                return

        await self._client.send_message(
            message.peer_id,
            send.message,
            reply_to=message.reply_to_msg_id,
        )

        await msg.delete()
        await self.client.delete_dialog("CDZ_AnswersBot")
