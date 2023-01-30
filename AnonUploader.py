__version__ = (0, 0, 1)
#   ___    _         _                             _         _                
#  (  _`\ ( )     _ ( )_                          ( )       (_ )              
#  | (_(_)| |__  (_)| ,_)     ___ ___     _      _| | _   _  | |    __    ___ 
#  `\__ \ |  _ `\| || |     /' _ ` _ `\ /'_`\  /'_` |( ) ( ) | |  /'__`\/',__)
#  ( )_) || | | || || |_    | ( ) ( ) |( (_) )( (_| || (_) | | | (  ___/\__, \
#  `\____)(_) (_)(_)`\__)   (_) (_) (_)`\___/'`\__,_)`\___/'(___)`\____)(____/
#
#     █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#     █▀█ █ █ █ █▀█ █▀▄ █
#
#      https://t.me/shitmodules | https://t.me/hikariatama
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: hikka_only
# scope: hikka_min 1.6.0

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/AnonUploader.jpg
# meta banner: https://te.legra.ph/file/bd8f3c2ab680d49df918b.mp4
# meta developer: @shitmodules

import imghdr
import io
import random
import re
import logging 

import requests
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import Message
from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class AnonUploader(loader.Module):
    """Anonymous file upload anonfiles.com"""

    strings = {
        "name": "AnonUploader",
        "noargs": "<i><b>🚫 File not specified {try to find replay photo}</i></b>",
        "err": "🚫 <i><b>Error uploading</i></b>",
        "unblock_bot": "<emoji document_id=5467928559664242360>❗️</emoji><i><b>@anonfiles_com_bot unblock this bot</i></b>",
        "not_an_image": "🚫 <i><b>This platform only supports images</i></b>",
        "uploading": "<emoji document_id=5213452215527677338>⏳</emoji><I><b>Uploading...</i></b>",
        "reply_pls": "<emoji document_id=5467928559664242360>❗️</emoji><i><b>Reply to photo</i></b>",
    }
    
    async def client_ready(self, client, db):
        self.db = db
        self.client = client
        post = (await client.get_messages("shitmodules", ids=33))
        await post.react("❤️")

    async def get_media(self, message: Message):
        reply = await message.get_reply_message()
        m = None
        if reply and reply.media:
            m = reply
        elif message.media:
            m = message
        elif not reply:
            await utils.answer(message, self.strings("noargs"))
            return False

        if not m:
            file = io.BytesIO(bytes(reply.raw_text, "utf-8"))
            file.name = "file.txt"
        else:
            file = io.BytesIO(await self._client.download_media(m, bytes))
            file.name = (
                m.file.name
                or (
                    "".join(
                        [
                            random.choice("abcdefghijklmnopqrstuvwxyz1234567890")
                            for _ in range(16)
                        ]
                    )
                )
                + m.file.ext
            )

        return file

    async def get_image(self, message: Message):
        file = await self.get_media(message)
        if not file:
            return False

        if imghdr.what(file) not in ["gif", "png", "jpg", "jpeg", "tiff", "bmp"]:
            await utils.answer(message, self.strings("not_an_image"))
            return False
            
        return file

    async def aimgcmd(self, message: Message):
        """> .aimg <reply to photo> - Anonymous file Uploader"""
        chat = "@anonfiles_com_bot"
        message = await utils.answer(message, self.strings("uploading"))
        file = await self.get_image(message)
        if not file:
          return

        async with self._client.conversation(chat) as conv:
            try:
                m = await conv.send_message(file=file)
                response = await conv.get_response()
            except YouBlockedUserError:
                await utils.answer(message, self.strings("unblock_bot"))
                return
            
            await self.client.delete_dialog(chat)
            
            try:
                url = (
                    re.search(
                        r'<meta property="og:image" data-react-helmet="true"'
                        r' content="(.*?)"',
                        (await utils.run_sync(requests.get, response.raw_text)).text,
                    )
                    .group(1)
                    .split("?")[0]
                )
            except Exception:
                url = response.raw_text
            await utils.answer(message, f"<i>🪄 Your file uploaded</i>: <code>{url}</code>")