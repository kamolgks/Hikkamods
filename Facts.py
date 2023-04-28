__version__ = (0, 0, 1)
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

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/Facts.jpeg
# meta banner: https://te.legra.ph/file/5133a6a7e4281e589c1ec.mp4

# meta developer: @shitmodules

import random
from asyncio import sleep
from .. import loader, utils
from hikkatl.tl.types import Message

channel = "interesnie_fac"

@loader.tds
class Facts(loader.Module):
    """interesting facts by @shitmodules"""

    strings = {
        "name": "Facts",
        "wait": "<emoji document_id=5472146462362048818>💡</emoji><b>Looking for something interesting for you...</b>",
    }

    strings_ru = {
        "wait": "<emoji document_id=5472146462362048818>💡</emoji><b>Ищу для тебя что-то интересное...</b>",
    }

    async def client_ready(self, client, db):
        self.db = db
        self.client = client
        self.messages = await self.client.get_messages(channel, limit=None)

    @loader.command(
        ru_doc="> Поищу для тебя какую нибудь интересную информацию)",
    )
    async def ifacts(self, message: Message):
        """
        > I'll look for some interesting information for you)
        """
        wtf = random.choice(self.messages)
        msg = await utils.answer(
            message, 
            self.strings["wait"],
        )

        await sleep(0.65)
        await msg.delete()
        await utils.answer(
            message, 
            wtf,
        )
