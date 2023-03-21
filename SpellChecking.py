__version__ = (0, 0, 2)
#   ___    _         _                             _         _                
#  (  _`\ ( )     _ ( )_                          ( )       (_ )              
#  | (_(_)| |__  (_)| ,_)     ___ ___     _      _| | _   _  | |    __    ___ 
#  `\__ \ |  _ `\| || |     /' _ ` _ `\ /'_`\  /'_` |( ) ( ) | |  /'__`\/',__)
#  ( )_) || | | || || |_    | ( ) ( ) |( (_) )( (_| || (_) | | | (  ___/\__, \
#  `\____)(_) (_)(_)`\__)   (_) (_) (_)`\___/'`\__,_)`\___/'(___)`\____)(____/
#                
#              © Copyright 2023
#
#          https://t.me/shitmodules
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: hikka_only
# scope: hikka_min 1.6.0

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/SpellChecking.png
# meta banner: https://te.legra.ph/file/fae1a26e0e47d369385e2.mp4
# meta developer: @shitmodules

import logging

from telethon.tl.types import Message
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class SpellChecking(loader.Module):
    """Check text for spelling errors by @shitmodules"""

    strings = {
        "name": "SpellChecking",
        "author": "shitmodules",
        "processing": (
            "<emoji document_id=5787344001862471785>✍️</emoji><i><b>Loading...</b></i>"
        ),
        "no_args": (
            "<emoji document_id=5215552806722738551>👎</emoji><i><b>There are no arguments or they are not enough!</b></i>"
        ),
        "unbl_bot" :(
            "<emoji document_id=5215557810359639942>⚠️</emoji>Unblock @Engy_Orthography_Bot bot"
        ),
    }
    
    strings_ru = {
        "processing": (
            "<emoji document_id=5787344001862471785>✍️</emoji><i><b>Загрузка...</b></i>"
        ),
        "no_args": (
            "<emoji document_id=5215552806722738551>👎</emoji><i><b>Нету аргументов или их недостаточно!</b></i>"
        ),
        "unbl_bot": (
            "<emoji document_id=5215557810359639942>⚠️</emoji>Разблокируй @Engy_Orthography_Bot бота"
        ),
    }

    strings_uz = {
        "ishlov berish": (
            "<emoji document_id=5787344001862471785>✍️</emoji><i><b>yuklanmoqda...</b></i>"
        ),
        "no_args": (
            "<emoji document_id=5215552806722738551>👎</emoji><i><b>argumentlar yo'q yoki ular etarli emas!</b></i>"
        ),
        "unbl_bot" :(
            "<emoji document_id=5215557810359639942>⚠️</emoji>Engy_Orthography_Bot botini blokdan chiqarish"
        ),
    }

    strings_kk = {
        "processing": (
            "<emoji document_id=5787344001862471785>>️</emoji><i><b > жүктеу...</b></i>"
        ),
        "no_args": (
            "<emoji document_id=5215552806722738551 >👎</emoji><i><b>дәлелдер жоқ немесе жеткіліксіз!</b></i>"
        ),
        "unbl_bot": (
            "<emoji document_id=5215557810359639942>⚠️</emoji>@Engy_Orthography_Bot ботының бұғатын алу"
        ),
    }

    @loader.command(
        ru_doc="> Проверяет текст на орфографические ошибки. (Количество аргументов не менее двух!)",
        kk_doc="> Мәтінді емле қателеріне тексереді. (Аргументтер саны екіден кем емес!)",
        uz_doc="> Matnni imlo xatolarini tekshiradi. (Argumentlar soni kamida ikkitasi!)",
    )
    async def orfgcmd(self, message: Message):
        """> Suggestion for checking spelling errors [args > 2]"""
        chat = "Engy_Orthography_Bot"
        args = utils.get_args_raw(message)
        if len(args) < 2:
            return await utils.answer(message, self.strings("no_args"))

        msg = await utils.answer(message, self.strings("processing"))

        async with self._client.conversation(chat) as conv:
            try:
                bot = []
                bot += [await conv.send_message(args)]
                send = await conv.get_response()
            except YouBlockedUserError:
                return await utils.answer(message, self.strings("unbl_bot"))

        await self._client.send_message(message.peer_id, send.message)
        await msg.delete()
        await self.client.delete_dialog(chat)
