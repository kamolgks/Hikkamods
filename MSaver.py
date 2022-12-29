__version__ = (1, 0, 0)
#   █▀▀▀█  █▀▄▀█ 
#   ▀▀▀▄▄  █  ▀ █   (shit mods)
#   █▄▄▄█  █     █
#                
#                © Copyright 2022
#
#          https://t.me/shitmodules
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: hikka_only
# scope: hikka_min 1.5.3
# meta developer: @shitmodules

from telethon import functions
from .. import utils, loader


chat = "@SaveAsBot"

class MSaverMod(loader.Module):
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
            "<emoji document_id=5199466698205306090>😤</emoji><b>Where is the link?</b>"
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
            "<emoji document_id=5199466698205306090>😤</emoji><b>А где ссылка?</b>"
        ),
    }

    @loader.command()
    async def imtcmd(self, message):
        """> .imt photo/video link"""
        url = utils.get_args_raw(message)
        if not url:
            return await utils.answer(message, self.strings("gde_link", message))
        message = await utils.answer(message, self.strings("processing"))
        async with self._client.conversation(chat) as conv:
                msgs = []
                msgs += [await conv.send_message("/start")]
                msgs += [await conv.get_response()]
                msgs += [await conv.send_message(url)]
                m = await conv.get_response()
            
        await self._client.send_file(message.peer_id, m.media, caption=self.strings("otl"), reply_to=message.reply_to_msg_id,)
        
        for msg in msgs + [m]:
            await msg.delete()

        if message.out:
            await message.delete()
            
        await message.client(
                functions.messages.DeleteHistoryRequest(
                    peer="SaveAsBot", max_id=0, just_clear=False, revoke=True
                ),
            )
