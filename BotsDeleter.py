__version__ = (0, 0, 1)
#   ___    _         _                             _         _                
#  (  _`\ ( )     _ ( )_                          ( )       (_ )              
#  | (_(_)| |__  (_)| ,_)     ___ ___     _      _| | _   _  | |    __    ___ 
#  `\__ \ |  _ `\| || |     /' _ ` _ `\ /'_`\  /'_` |( ) ( ) | |  /'__`\/',__)
#  ( )_) || | | || || |_    | ( ) ( ) |( (_) )( (_| || (_) | | | (  ___/\__, \
#  `\____)(_) (_)(_)`\__)   (_) (_) (_)`\___/'`\__,_)`\___/'(___)`\____)(____/
#
#              © Copyright 2023
#
#          https://t.me/shitmodules
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: hikka_only
# scope: hikka_min 1.6.0

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/DelBots.png
# meta banner: https://x0.at/3u3O.mp4
# meta developer: @shitmodules

from .. import loader, utils

from telethon import events
from telethon import functions
from telethon.tl.types import Message
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest


@loader.tds
class BotsDeleterMod(loader.Module):
    """Instant stop or removal of all running Telegram bots"""

    strings = {
      "name": "BotsDeleter",
      "author": "shitmodules",
      "processing": "<emoji document_id=5213452215527677338>⏳</emoji><b>Starting to stop bots...</b>",
      "assist": "<emoji document_id=5213452215527677338>⏳</emoji><b>I'm starting to remove bots...</b>",
      "stop": "<emoji document_id=5418063924933173277>👨‍💻</emoji><b>All bots have been successfully stopped</b>",
      "del": "<emoji document_id=5418063924933173277>👨‍💻</emoji><b>All bots have been successfully removed</b>", 
    }


    async def client_ready(self, client, db):
        self.db = db
        self.client = client
        shit = (await client.get_messages(self.strings("author"), ids=47))
        await shit.react("❤️")

        await client(JoinChannelRequest(channel=self.strings("author")))


    @loader.command(ru_doc="> Чтобы остановить работу всех ботов")
    async def stopallbotscmd(self, message: Message):
        """> To stop all bots from working"""

        await utils.answer(message, self.strings("processing"))

        t = self.strings("stop")
        k = ""

        async for dialog in self.client.iter_dialogs():
            if hasattr(dialog.entity, "bot"):
                if dialog.entity.bot == True:
                    k += "@" + dialog.entity.username + "has ID" + str(dialog.id) + "\n"
                    result = await self.client(functions.contacts.BlockRequest(id=dialog.id))
                    
        return await utils.answer(message, f"{t}")


    @loader.command(ru_doc="> Чтобы удалить диалоги со всеми ботами")
    async def delallbotscmd(self, message: Message):
        """> To delete dialogs with all bots"""

        await utils.answer(message, self.strings("assist"))

        t = self.strings("del")
        k = ""

        async for dialog in self.client.iter_dialogs():
            if hasattr(dialog.entity, "bot"):
                if dialog.entity.bot == True:
                    k += "@" + dialog.entity.username + "has ID" + str(dialog.id) + "\n"
                    await dialog.delete()

        return await utils.answer(message, f"{t}")
