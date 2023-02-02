__version__ = (0, 0, 2)
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

# meta banner: https://x0.at/NqCK.gif
# meta developer: @shitmodules

from .. import loader, utils
from telethon.tl.types import Message
import random

chat = "anertsy"

@loader.tds
class AnecdoteGenerator(loader.Module):
    """Anecdote generator by @shitmodules"""

    strings = {
        "name": "AnecdoteGenerator",
        "author": "shitmodules",
    }

    async def client_ready(self, client, db):
        self.db = db
        self.client = client
        post = (await client.get_messages("shitmodules", ids=14))
        await post.react("❤️")
        await client(JoinChannelRequest(channel=self.strings("author")))

    async def client_ready(self):
        self.messages = await self.client.get_messages(chat, limit=None)

    @loader.command(ru_doc="Генерирует анекдоты (они не всегда смешные)")
    async def aneccmd(self, message: Message):
        """Sends an anecdote (not always funny)"""
        wtf = random.choice(self.messages)
        await utils.answer(message, wtf)
