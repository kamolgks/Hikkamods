__version__ = (0, 0, 8)
#   ___    _         _                             _         _                
#  (  _`\ ( )     _ ( )_                          ( )       (_ )              
#  | (_(_)| |__  (_)| ,_)     ___ ___     _      _| | _   _  | |    __    ___ 
#  `\__ \ |  _ `\| || |     /' _ ` _ `\ /'_`\  /'_` |( ) ( ) | |  /'__`\/',__)
#  ( )_) || | | || || |_    | ( ) ( ) |( (_) )( (_| || (_) | | | (  ___/\__, \
#  `\____)(_) (_)(_)`\__)   (_) (_) (_)`\___/'`\__,_)`\___/'(___)`\____)(____/
#                
#              © Copyright 2022
#
#          https://t.me/shitmodules
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: hikka_only
# scope: hikka_min 1.5.3

# meta banner: https://x0.at/c9cJ.mp4
# meta developer: @shitmodules

import logging

from time import sleep
from telethon import functions
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import utils, loader

logger = logging.getLogger(__name__)

@loader.tds
class MultiSaver(loader.Module):
    """Download video, photo from instagram, TikTok and Pinterest"""

    strings = {
        "name": "MultiSaver",
        "processing": (
            "<emoji document_id=5346152548761868765>💜</emoji><i><b>Processing...</i></b>"
        ),
        "otl": (
            "<emoji document_id=5472104053854968558>❤</emoji><i><b>Successfuly downloaded</i></b>"
        ),
        "gde_link": (
            "<emoji document_id=5215552806722738551>👎</emoji><i><b>Where is the link?</i></b>"
        ),
        "unl_bot" :(
            "<emoji document_id=5215557810359639942>⚠️</emoji>Unblock @saveasbot bot"
        ),
    }

    strings_ru = {
        "processing": (
            "<emoji document_id=5346152548761868765>💜</emoji><i><b>Загрузка...</i></b>"
        ),
        "otl": (
            "<emoji document_id=5472104053854968558>❤</emoji><i><b>Успешно загружено</i></b>"
        ),
        "gde_link": (
            "<emoji document_id=5215552806722738551>👎</emoji><i><b>А где ссылка?</i></b>"
        ),
        "unl_bot": (
            "<emoji document_id=5215557810359639942>⚠️</emoji>Разблокируй @saveasbot бота"
        ),
    }

    strings_uz = {
        "processing": (
            "<emoji document_id=5346152548761868765>💜</emoji><i><b>Yuklanmoqda...</i></b>"
        ),
        "otl": (
            "<emoji document_id=5472104053854968558>❤</emoji><i><b>Muvaffaqiyatli yuklab olindi</i></b>"
        ),
        "gde_link": (
            "<emoji document_id=5215552806722738551>👎</emoji><i><b>Havola qani?</i></b>"
        ),
        "unl_bot" :(
            "<emoji document_id=5215557810359639942>⚠️</emoji>@saveasbot botini blokdan chiqarish"
        ),
    }

    async def client_ready(self, client, db):
        self.db = db
        self.client = client
        post = (await client.get_messages("shitmodules", ids=10))
        await post.react("❤️")


    @loader.command(
        ru_doc="> .imt Скачать фото/видео из инстаграм, Тик ток и Пинтереста",
        uz_doc="> .imt Foto/videoni instagram, tik tok va pinterestdan yuklab oling",
    )
    async def imtcmd(self, message):
        """> .imt photo/video link"""
        url = utils.get_args_raw(message)
        if not url:
            return await utils.answer(message, self.strings("gde_link", message))
        proc = await utils.answer(message, self.strings("processing"))

        async with self._client.conversation("SaveAsBot") as conv:
            try:
                bot = []
                bot += [await conv.send_message(url)]
                priem = await conv.get_response()
            except YouBlockedUserError:
                return await utils.answer(message, self.strings("unl_bot"))

        await self._client.send_file(
            message.peer_id,
            priem.media,
            caption=self.strings("otl"),
            reply_to=message.reply_to_msg_id,
        )

        await proc.delete()

        sleep(1)

        await self.client.delete_dialog("SaveAsBot")
