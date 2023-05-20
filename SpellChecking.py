__version__ = (0, 0, 3)

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

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/SpellChecking.png
# meta banner: http://devs.farkhodovme.tk/bannerget/kamolgks/spellchecking.png

# meta developer: @shitmodules

import logging

from telethon.tl.types import Message
from asyncio.exceptions import TimeoutError
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class SpellCheckingMod(loader.Module):
    """Check text for spelling errors by @shitmodules"""

    strings = {
        "name": "SpellChecking",
        "processing": (
            "<emoji document_id=5787344001862471785>✍️</emoji><b>Loading...</b>"
        ),
        "no_args": (
            "<emoji document_id=5215552806722738551>👎</emoji><b>There are no arguments or they are not enough!</b>"
        ),
        "unl_bot": (
            "<emoji document_id=5215557810359639942>⚠️</emoji>Unlock @SpellCheckBot"
        ),
        "time_err": (
            "<emoji document_id=5280821895711697516>⛔️</emoji><b>The waiting time has expired.</b> "
            "<b>Either the bot is loaded, or it's dead. Try again a little later</b>"
        ),
    }

    strings_ru = {
        "processing": (
            "<emoji document_id=5787344001862471785>✍️</emoji><b>Загрузка...</b>"
        ),
        "no_args": (
            "<emoji document_id=5215552806722738551>👎</emoji><b>Нету аргументов или их недостаточно!</b>"
        ),
        "unl_bot": (
            "<emoji document_id=5215557810359639942>⚠️</emoji>Разблокируй @SpellCheckBot"
        ),
        "time_err": (
            "<emoji document_id=5280821895711697516>⛔️</emoji><b>Истекло время ожидания.</b> "
            "<b>Либо бот нагружен, либо он умер. Попробуйте немного позже.</b>"
        ),
    }

    strings_uz = {
        "processing": (
            "<emoji document_id=5787344001862471785>✍️</emoji><b>yuklanmoqda...</b>"
        ),
        "no_args": (
            "<emoji document_id=5215552806722738551>👎</emoji><b>argumentlar yo'q yoki ular etarli emas!</b>"
        ),
        "unl_bot": (
            "<emoji document_id=5215557810359639942>⚠️</emoji>@SpellCheckBot botini blokdan chiqarish"
        ),
        "time_err": (
            "<emoji document_id=5280821895711697516>⛔️</emoji>Kutish vaqti tugadi.</b> "
            "<b>Yoki bot Yuklangan yoki u vafot etgan. Birozdan keyin sinab ko'ring."
        ),
    }

    strings_kk = {
        "processing": (
            "<emoji document_id=5787344001862471785>>️</emoji><b > жүктеу...</b>"
        ),
        "no_args": (
            "<emoji document_id=5215552806722738551 >👎</emoji><b>дәлелдер жоқ немесе жеткіліксіз!</b>"
        ),
        "unl_bot": (
            "<emoji document_id=5215557810359639942>⚠️</emoji>@SpellCheckBot ботының бұғатын алу"
        ),
        "time_err": (
            "<emoji document_id=5280821895711697516>⛔️</emoji><b>Күту уақыты аяқталды.</b> "
            "<b>Не бот жүктелген, не ол қайтыс болды. Сәл кейінірек көріңіз.</b>"
        ),
    }

    @loader.command(
        ru_doc="> Проверяет текст на орфографические ошибки.",
        kk_doc="> Мәтінді емле қателеріне тексереді.",
        uz_doc="> Matnni imlo xatolarini tekshiradi.",
    )
    async def orfgcmd(self, message: Message):
        """> Suggestion for checking spelling errors"""

        chat = "@SpellCheckBot"
        args = utils.get_args_raw(message)

        if len(args) < 2:
            await utils.answer(message, self.strings("no_args"))
            return

        msg = await utils.answer(message, self.strings("processing"))

        async with self._client.conversation(chat) as conv:
            try:
                bot = []
                bot += [await conv.send_message(args)]
                bot += [await conv.get_response()]
                response = await conv.get_response()
            except YouBlockedUserError:
                await utils.answer(message, self.strings("unl_bot"))
                return

            except TimeoutError:
                await utils.answer(message, self.strings("time_err"))
                return

            if response.text:
                await self._client.send_message(
                    message.to_id,
                    response.text,
                    reply_to=message.reply_to_msg_id,
                )

            await msg.delete()
            await self.client.delete_dialog(chat)
