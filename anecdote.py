__version__ = (1, 0, 0)
#   █▀▀▀█  █▀▄▀█ 
#   ▀▀▀▄▄  █  ▀ █   (𝐒𝐡𝐢𝐭 𝐦𝐨𝐝𝐬)
#   █▄▄▄█  █     █
#        
#            © Copyright 2022
#
#          https://t.me/shitmodules
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @shitmodules

from .. import loader, utils
from telethon.tl.types import Message
import random

chat = "anertsy"

@loader.tds
class Anecdote(loader.Module):

    strings = {
        "name": "Anecdote♤",
    }
    
    async def client_ready(self):
    	self.messages = await self.client.get_messages(chat, limit=100)

    @loader.command()
    async def aneccmd(self, message: Message):
        """Sends an anecdote (not always funny) by @shitmodules"""
        wtf = random.choice(self.messages)
        await utils.answer(message, wtf)
