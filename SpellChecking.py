__version__ = (0, 0, 1)
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

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class SpellChecking(loader.Module):
    """Check text for spelling errors by @shitmodules"""

    strings = {
        "name": "SpellChecking",
        "processing": (
            "<emoji document_id=5787344001862471785>✍️</emoji><i><b>Loading...</b></i>"
        ),
        "no_args": (
            "<emoji document_id=5215552806722738551>👎</emoji><i><b>There are no arguments or they are not enough!</b></i>"
        ),
    }
    
    strings_ru = {
        "processing": (
            "<emoji document_id=5787344001862471785>✍️</emoji><i><b>Загрузка...</b></i>"
        ),
        "no_args": (
            "<emoji document_id=5215552806722738551>👎</emoji><i><b>Нету аргументов или их недостаточно!</b></i>"
        ),
    }

    strings_kz = {
        "processing": (
            "<emoji document_id=5787344001862471785>>️</emoji><i><b > жүктеу...</b></i>"
        ),
        "no_args": (
            "<emoji document_id=5215552806722738551 > 👎< / emoji><i > <b>дәлелдер жоқ немесе жеткіліксіз!</b></i>"
        ),
    }

    strings_uz = {
        "ishlov berish": (
            "<emoji document_id=5787344001862471785>✍️</emoji><i><b>yuklanmoqda...</b></i>"
        ),
        "no_args": (
            "<emoji document_id=5215552806722738551>👎</emoji><i><b>argumentlar yo'q yoki ular etarli emas!</b></i>"
        ),
    }

    strings_tr = {
        "processing": (
            "<emoji document_id=5787344001862471785>✍️</emoji><i><b>indiriliyor...</b></i>"
        ),
        "no_args": (
            "<emoji document_id=5215552806722738551>👎</emoji><i><b>Argüman yok veya yeterli değil!</b></i>"
        ),
    }

    async def client_ready(self, client, db):
        self.db = db
        self.client = client
        post = (await client.get_messages("shitmodules", ids=29))
        await post.react("❤️")

    @loader.command(
        ru_doc="Проверяет текст на орфографические ошибки. (Количество аргументов не менее двух!)",
        kz_doc="Мәтінді емле қателеріне тексереді. (Аргументтер саны екіден кем емес!)",
        tr_doc="Metni yazım hataları için doğrular. (En az iki argüman sayısı!)",
        uz_doc="Matnni imlo xatolarini tekshiradi. (Argumentlar soni kamida ikkitasi!)",
    )
    async def orfgcmd(self, message: Message):
        """> .orfg <Suggestion for checking spelling errors> {args > 2}"""
        chat = "Engy_Orthography_Bot"
        args = utils.get_args_raw(message)
        if len(args) < 2:
            return await utils.answer(message, self.strings("no_args"))
        message = await utils.answer(message, self.strings("processing"))
        async with self._client.conversation(chat) as conv:
            msgs = []
            msgs += [await conv.send_message("/start")]
            msgs += [await conv.get_response()]
            msgs += [await conv.send_message(args)]
            m = await conv.get_response()

        await self._client.send_message(
            message.peer_id,
            m.message,
            reply_to=message.reply_to_msg_id,
        )
        
        for msg in msgs + [m]:
            await msg.delete()

        if message.out:
            await message.delete()
            
        await self.client.delete_dialog(chat)