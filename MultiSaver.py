__version__ = (0, 0, 6)
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
# scope: hikka_min 1.6.0
# meta banner: https://x0.at/c9cJ.mp4
# meta developer: @shitmodules

from .. import utils, loader
import logging

logger = logging.getLogger(__name__)

@loader.tds
class MultiSaverMod(loader.Module):
    """Download video, photo from instagram, TikTok and Pinterest"""

    strings = {
        "name": "MultiSaver",
        "processing": (
            "<emoji document_id=5346152548761868765>💜</emoji><b>Processing...</b>"
        ),
        "otl": (
            "<emoji document_id=5472104053854968558>❤</emoji><b>Successfuly downloaded</b>"
        ),
        "gde_link": (
            "<emoji document_id=5348548199915200824>🔫</emoji><b>Where is the link?</b>"
        ),
    }

    strings_ru = {
        "processing": (
            "<emoji document_id=5346152548761868765>💜</emoji><b>Загрузка...</b>"
        ),
        "otl": (
            "<emoji document_id=5472104053854968558>❤</emoji><b>Успешно загружено</b>"
        ),
        "gde_link": (
            "<emoji document_id=5348548199915200824>🔫</emoji><b>А где ссылка?</b>"
        ),
    }

    strings_uz = {
        "processing": (
            "<emoji document_id=5346152548761868765>💜</emoji><b>Yuklanmoqda...</b>"
        ),
        "otl": (
            "<emoji document_id=5472104053854968558>❤</emoji><b>Muvaffaqiyatli yuklab olindi</b>"
        ),
        "gde_link": (
            "<emoji document_id=5348548199915200824>🔫</emoji><b>Havola qani?</b>"
        ),
    }

    strings_hi = {
        "processing": (
            "<emoji document_id=5346152548761868765>💜</emoji><b>लोड हो रहा है । ..</b>"
        ),
        "otl": (
            "<emoji document_id=5472104053854968558>❤</emoji><b>सफलतापूर्वक अपलोड किया गया</b>"
        ),
        "gde_link": (
            "<emoji document_id=5348548199915200824>🔫</emoji><b>और लिंक कहां है?</b>"
        ),
    }

    @loader.command("> .ins ссылка на видео/фото | Скачать видео/фото из инсты")
    async def inscmd(self, message):
        """> .ins photo/video link | Download video/image from Instagram"""
        url = utils.get_args_raw(message)
        if not url:
            return await utils.answer(message, self.strings("gde_link", message))
        message = await utils.answer(message, self.strings("processing"))
        async with self._client.conversation("savezbot") as conv:
                msgs = []
                msgs += [await conv.send_message("/start")]
                msgs += [await conv.get_response()]
                msgs += [await conv.send_message(url)]
                m = await conv.get_response()
            
        await self._client.send_file(
            message.peer_id,
            m.media,
            caption=self.strings("otl"),
            reply_to=message.reply_to_msg_id,
        )

        for msg in msgs + [m]:
            await msg.delete()

        if message.out:
            await message.delete()

        await self.client.delete_dialog("savezbot")
            
          
    @loader.command(ru_doc="> .tts ссылка на видео | Скачать видео из Тик Тока")
    async def ttscmd(self, message):
      """> .tts video link | Download video from Tik-Tok"""
      url = utils.get_args_raw(message)
      if not url:
        await utils.answer(message, self.strings("gde_link"))
        return 
      message = await utils.answer(message, self.strings("processing"))
      async with self._client.conversation("saveit_tt_bot") as conv:
        msgs = []
        msgs += [await conv.send_message("/start")]
        msgs += [await conv.get_response()]
        msgs += [await conv.send_message(url)]
        m = await conv.get_response()

        await self._client.send_file(
            message.peer_id,
            m.media,
            caption=self.strings("otl"),
            reply_to=message.reply_to_msg_id,
        )
        
        for msg in msgs + [m]:
            await msg.delete()

        if message.out:
            await message.delete()
           
        await self.client.delete_dialog("saveit_tt_bot")


    @loader.command(ru_doc="> .pin ссылка на видео | Скачать видео из Pinterest")
    async def pincmd(self, message):
        """> .pin video link | Download video from Pinterest"""
        url = utils.get_args_raw(message)
        if not url:
            await utils.answer(message, self.strings("gde_link"))
            return
        message = await utils.answer(message, self.strings("processing"))
        async with self._client.conversation("saveasbot") as conv:
            msgs = []
            msgs += [await conv.send_message("/start")]
            msgs += [await conv.get_response()]
            msgs += [await conv.send_message(url)]
            m = await conv.get_response()

        await self._client.send_file(
            message.peer_id,
            m.media,
            caption=self.strings("otl"),
            reply_to=message.reply_to_msg_id,
        )
        
        for msg in msgs + [m]:
            await msg.delete()

        if message.out:
            await message.delete()
            
        await self.client.delete_dialog("saveasbot")
