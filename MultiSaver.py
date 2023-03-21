__version__ = (0, 0, 8)
#   ___    _         _                             _         _                
#  (  _`\ ( )     _ ( )_                          ( )       (_ )              
#  | (_(_)| |__  (_)| ,_)     ___ ___     _      _| | _   _  | |    __    ___ 
#  `\__ \ |  _ `\| || |     /' _ ` _ `\ /'_`\  /'_` |( ) ( ) | |  /'__`\/',__)
#  ( )_) || | | || || |_    | ( ) ( ) |( (_) )( (_| || (_) | | | (  ___/\__, \
#  `\____)(_) (_)(_)`\__)   (_) (_) (_)`\___/'`\__,_)`\___/'(___)`\____)(____/
#                
#              © Copyright 2022/2023
#
#          https://t.me/shitmodules
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: hikka_only
# scope: hikka_min 1.6.0

# meta pic: 
# meta banner: 
# meta developer: @shitmodules

import logging
import asyncio

from telethon.tl.types import Message
from asyncio.exceptions import TimeoutError
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import utils, loader

logger = logging.getLogger(__name__)

@loader.tds
class MultiSaver(loader.Module):
    """Download video, photo from instagram, TikTok and Pinterest"""

    strings = {
        "name": "MultiSaver",
        "author": "shitmodules",
        "processing": (
            "<emoji document_id=5346152548761868765>💜</emoji><b>Processing...</b>"
        ),
        "successfully": (
            "<emoji document_id=5472104053854968558>❤</emoji><b>Successfuly downloaded<</b>"
        ),
        "where_link": (
            "<emoji document_id=5215552806722738551>👎</emoji><b>Where is the link?</b>"
        ),
        "unblock_bot" :(
            "<emoji document_id=5215557810359639942>⚠️</emoji><b>Unblock @saveasbot bot</b>"
        ),
        "time_err": (
            "<emoji document_id=5269492338920528466>😱</emoji>"
            "<b>The waiting time has expired, either the video is too long, or the bot is heavily loaded. Be patient!</b>"
        ),
    }

    strings_ru = {
        "processing": (
            "<emoji document_id=5346152548761868765>💜</emoji><b>Загрузка...</b>"
        ),
        "successfully": (
            "<emoji document_id=5472104053854968558>❤</emoji><b>Успешно загружено</b>"
        ),
        "where_link": (
            "<emoji document_id=5215552806722738551>👎</emoji><b>А где ссылка?</b>"
        ),
        "unblock_bot": (
            "<emoji document_id=5215557810359639942>⚠️</emoji><b>Разблокируй @saveasbot бота</b>"
        ),
        "time_err": (
            "<emoji document_id=5269492338920528466>😱</emoji>"
            "<b>Истекло время ожидания, либо видос слишком длинный, либо бот сильно нагружен. Наберись терпения!</b>"
        ),
    }

    strings_uz = {
        "processing": (
            "<emoji document_id=5346152548761868765>💜</emoji><b>Yuklanmoqda...</b>"
        ),
        "successfully": (
            "<emoji document_id=5472104053854968558>❤</emoji><b>Muvaffaqiyatli yuklab olindi.</b>"
        ),
        "where_link": (
            "<emoji document_id=5215552806722738551>👎</emoji><b>Havola qani?</b>"
        ),
        "unblock_bot" :(
            "<emoji document_id=5215557810359639942>⚠️</emoji><b>@saveasbot botini blokdan chiqarish</b>"
        ),
        "time_err": (
            "<emoji document_id=5269492338920528466>😱</emoji>"
            "<b>Kutish vaqti tugadi, yoki video juda uzun yoki bot og'ir yuklangan. Sabr qiling!</b>"
        ),
    }


    @loader.command(
        ru_doc="> Скачать фото/видео из инстаграм, Тик ток и Пинтереста",
        uz_doc="> Foto/videoni instagram, tik tok va pinterestdan yuklab oling",
    )
    async def imtcmd(self, message: Message):
        """> photo/video link"""
        chat = "saveasbot"
        url = utils.get_args_raw(message)
        if not url:
            return await utils.answer(message, self.strings("where_link", message))

        msg = await utils.answer(message, self.strings("processing"))

        async with self._client.conversation(chat) as conv:
            try:
                bot = []
                bot += [await conv.send_message(url)]
                send = await conv.get_response()
            except YouBlockedUserError:
                return await utils.answer(message, self.strings("unblock_bot"))

        await self._client.send_file(
            message.peer_id,
            send.media,
            caption=self.strings("successfully"),
            reply_to=message.reply_to_msg_id,
        )

        await msg.delete()
        await asyncio.sleep(1)
        await self.client.delete_dialog(chat)
