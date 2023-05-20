__version__ = (1, 0, 9)
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

# meta pic: https://te.legra.ph/file/9fbbf3676de7a1e844e56.jpg
# meta banner: http://devs.farkhodovme.tk/bannerget/kamolgks/multisaver.png

# meta developer: @shitmodules

import logging
import asyncio

from telethon.tl.types import Message
from asyncio.exceptions import TimeoutError
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class MultiSaverMod(loader.Module):
    """Download video, photo from instagram, TikTok and Pinterest"""

    strings = {
        "name": "MultiSaver",
        "processing": (
            "<emoji document_id=5190568934717270805>🙂</emoji><b>Processing...</b>"
        ),
        "successfully": (
            "<emoji document_id=5379619324774326601>😏</emoji><b>Successfuly downloaded</b>"
        ),
        "where-link": (
            "<emoji document_id=5280821895711697516>⛔️</emoji><b>Where is the link?</b>"
        ),
        "unl-bot": (
            "<emoji document_id=5215557810359639942>⚠️</emoji><b>Unlock @saveasbot bot</b>"
        ),
        "time-err": (
            "<emoji document_id=5269492338920528466>😱</emoji>"
            "<b>The waiting time has expired, either the video is too long, or the bot is heavily loaded. Be patient!</b>"
        ),
    }

    strings_ru = {
        "processing": (
            "<emoji document_id=5190568934717270805>🙂</emoji><b>Загрузка...</b>"
        ),
        "successfully": (
            "<emoji document_id=5379619324774326601>😏</emoji><b>Успешно загружено</b>"
        ),
        "where-link": (
            "<emoji document_id=5280821895711697516>⛔️</emoji><b>А где ссылка?</b>"
        ),
        "unl-bot": (
            "<emoji document_id=5215557810359639942>⚠️</emoji><b>Разблокируй @saveasbot бота</b>"
        ),
        "time-err": (
            "<emoji document_id=5269492338920528466>😱</emoji>"
            "<b>Истекло время ожидания, либо видос слишком длинный, либо бот сильно нагружен. Наберись терпения!</b>"
        ),
    }

    strings_uz = {
        "processing": (
            "<emoji document_id=5190568934717270805>🙂</emoji><b>Yuklanmoqda...</b>"
        ),
        "successfully": (
            "<emoji document_id=5379619324774326601>😏</emoji><b>Muvaffaqiyatli yuklab olindi.</b>"
        ),
        "where-link": (
            "<emoji document_id=5280821895711697516>⛔️</emoji><b>Havola qani?</b>"
        ),
        "unl-bot": (
            "<emoji document_id=5215557810359639942>⚠️</emoji><b>@saveasbot botini blokdan chiqarish</b>"
        ),
        "time-err": (
            "<emoji document_id=5269492338920528466>😱</emoji>"
            "<b>Kutish vaqti tugadi, yoki video juda uzun yoki bot og'ir yuklangan. Sabr qiling!</b>"
        ),
    }

    strings_tr = {
        "processing": (
            "<emoji document_id=5190568934717270805>🙂</emoji><b>İşleme...</b>"
        ),
        "successfully": (
            "<emoji document_id=5379619324774326601>😏</emoji><b>Başarıyla indirildi</b>"
        ),
        "where-link": (
            "<emoji document_id=5280821895711697516>⛔️</emoji><b>Bağlantı nerede?</b>"
        ),
        "unl-bot": (
            "<emoji document_id=5215557810359639942>⚠️</emoji><b>@saveasbot botunun kilidini aç</b>"
        ),
        "time-err": (
            "<emoji document_id=5269492338920528466>😱</emoji>"
            "<b>Bekleme süresi doldu, ya video çok uzun ya da bot çok yüklü. Sabırlı ol!</b>"
        ),
    }

    @loader.group_member
    @loader.command(
        ru_doc="> Скачать фото/видео из инстаграм, Тик ток и Пинтереста",
        uz_doc="> Foto/videoni instagram, tik tok va pinterestdan yuklab oling",
        tr_doc="> İnstagram, Tick Tok ve Pinterest'ten fotoğraf /video indirin",
    )
    async def imtcmd(self, message: Message):
        """> photo/video link"""

        chat = "@SaveAsBot"
        url = utils.get_args_raw(message)

        if not url:
            await utils.answer(message, self.strings("where-link"))
            return

        msg = await utils.answer(message, self.strings("processing"))

        async with self._client.conversation(chat) as conv:
            try:
                bot = []
                bot += [await conv.send_message(url)]
                response = await conv.get_response()
            except YouBlockedUserError:
                await utils.answer(message, self.strings("unl-bot"))
                return

            except TimeoutError:
                await utils.answer(message, self.strings("time-err"))
                return

            if response.media:
                await self._client.send_file(
                    message.to_id,
                    response.media,
                    caption=self.strings("successfully"),
                    reply_to=message.reply_to_msg_id,
                )

        await msg.delete()
        await asyncio.sleep(1)

        await self.client.delete_dialog(chat)
