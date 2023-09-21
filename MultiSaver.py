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
# *            © Copyright 2022/2023
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
# meta banner: https://raw.githubusercontent.com/kamolgks/assets/main/MultiSaver.jpg

# meta developer: @shitmodules

import asyncio
import logging
from asyncio.exceptions import TimeoutError

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import Message

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class MultiSaverMod(loader.Module):
    """Download video, photo from instagram, TikTok and Pinterest"""

    strings = {
        "name": "MultiSaver",
        "loading": (
            "<emoji document_id=5190568934717270805>🙂</emoji><b>Loading...</b>"
        ),
        "successfully": (
            "<emoji document_id=5974141780357025338>⬇️</emoji><b>Successfully downloaded</b>"
        ),
        "noargs": (
            "<emoji document_id=5972201876773408053>🚫</emoji><b>Where is the link?</b>"
        ),
        "unl_bot": (
            "<emoji document_id=5972201876773408053>🚫</emoji><b>Unlock @saveasbot</b>"
        ),
        "time_err": (
            "<emoji document_id=5972201876773408053>🚫</emoji>"
            "<b>The waiting time has expired, either the video is too long, or the bot is heavily loaded. Be patient!</b>"
        ),
    }

    strings_ru = {
        "loading": (
            "<emoji document_id=5190568934717270805>🙂</emoji><b>Загрузка...</b>"
        ),
        "successfully": (
            "<emoji document_id=5974141780357025338>⬇️</emoji><b>Успешно загружено</b>"
        ),
        "noargs": (
            "<emoji document_id=5972201876773408053>🚫</emoji><b>А где ссылка?</b>"
        ),
        "unl_bot": (
            "<emoji document_id=5972201876773408053>🚫</emoji><b>Разблокируй @saveasbot</b>"
        ),
        "time_err": (
            "<emoji document_id=5972201876773408053>🚫</emoji>"
            "<b>Истекло время ожидания, либо видос слишком длинный, либо бот сильно нагружен. Наберись терпения и попробуй попозже!</b>"
        ),
    }

    strings_uz = {
        "loading": (
            "<emoji document_id=5190568934717270805>🙂</emoji><b>Yuklanmoqda...</b>"
        ),
        "successfully": (
            "<emoji document_id=5974141780357025338>⬇️</emoji><b>Muvaffaqiyatli yuklab olindi.</b>"
        ),
        "noargs": (
            "<emoji document_id=5972201876773408053>🚫</emoji><b>Havola qani?</b>"
        ),
        "unl_bot": (
            "<emoji document_id=5972201876773408053>🚫</emoji><b>@saveasbot ni blokdan chiqarish</b>"
        ),
        "time_err": (
            "<emoji document_id=5972201876773408053>🚫</emoji>"
            "<b>Kutish vaqti tugadi, yoki video juda uzun yoki bot og'ir yuklangan. Sabr qilib, birozdan keyin urinib ko'ring!</b>"
        ),
    }

    strings_tr = {
        "loading": (
            "<emoji document_id=5190568934717270805>🙂</emoji><b>İşleme...</b>"
        ),
        "successfully": (
            "<emoji document_id=5974141780357025338>⬇️</emoji><b>Başarıyla indirildi</b>"
        ),
        "noargs": (
            "<emoji document_id=5972201876773408053>🚫</emoji><b>Bağlantı nerede?</b>"
        ),
        "unl_bot": (
            "<emoji document_id=5972201876773408053>🚫</emoji><b>@saveasbot botunun kilidini aç</b>"
        ),
        "time_err": (
            "<emoji document_id=5972201876773408053>🚫</emoji>"
            "<b>Bekleme süresi doldu, ya video çok uzun ya da bot çok yüklü. Sabırlı ol!</b>"
        ),
    }

    @loader.group_member
    @loader.command(
        ru_doc="> Ссылка на фото/видео",
        uz_doc="> Foto/video havolasi",
        tr_doc="> fotoğraflara/videolara bağlantılar",
    )
    async def imt(self, message: Message):
        """> photo/video link"""
        chat = "@SaveAsBot"
        args = utils.get_args_raw(message)
        if len(args) == 0:
            return await utils.answer(message, self.strings["noargs"])

        msg = await utils.answer(message, self.strings["loading"])
        async with self._client.conversation(chat) as conv:
            try:
                bot = []
                bot += [await conv.send_message(args)]
                response = await conv.get_response()
            except YouBlockedUserError:
                return await utils.answer(message, self.strings["unl_bot"])
            except TimeoutError:
                return await utils.answer(message, self.strings["time_err"])

            if response.media:
                await self._client.send_file(
                    message.to_id,
                    response.media,
                    caption=self.strings["successfully"],
                    reply_to=message.reply_to_msg_id,
                )

        await msg.delete()
        await asyncio.sleep(0.64)
        await self.client.delete_dialog(chat)
