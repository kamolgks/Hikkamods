__version__ = (0, 0, 1)
#   ___    _         _                             _         _                
#  (  _`\ ( )     _ ( )_                          ( )       (_ )              
#  | (_(_)| |__  (_)| ,_)     ___ ___     _      _| | _   _  | |    __    ___ 
#  `\__ \ |  _ `\| || |     /' _ ` _ `\ /'_`\  /'_` |( ) ( ) | |  /'__`\/',__)
#  ( )_) || | | || || |_    | ( ) ( ) |( (_) )( (_| || (_) | | | (  ___/\__, \
#  `\____)(_) (_)(_)`\__)   (_) (_) (_)`\___/'`\__,_)`\___/'(___)`\____)(____/
                                                                                                                                                     
#
#            © Copyright 2022
#
#          https://t.me/shitmodules
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: hikka_only
# scope: hikka_min 1.6.0

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/HighlyPaidProfessions.jpg
# meta banner: https://x0.at/qGYX.gif
# meta developer: @shitmodules

import random

from .. import loader, utils
from telethon.tl.types import Message
from time import sleep

@loader.tds
class HighlyPaidProfessions(loader.Module):
  """Throws off information about the highest paid professions in the world. (Maybe someone will need)"""
  
  strings = {
    "name": "HighlyPaidProfessions",
    "wait": "<emoji document_id=5213452215527677338>⏳</emoji><b>Processing...</b>",
  }
  
  strings_ru = {
    "wait": "<emoji document_id=5213452215527677338>⏳</emoji><b>Загрузка...</b>",
  }

  strings_uz = {
    "wait": "<emoji document_id=5213452215527677338>⏳</emoji><b>Yuklanmoqda...</b>",
  }

  async def client_ready(self):
        self.messages = await self.client.get_messages(chat, limit=None)
  
  @loader.command(ru_doc="Самые высокооплачиваемые профессии в мире")
  async def profscmd(self, message: Message):
    """.profs The highest paid professions in the world"""

    chat = "prfhgd"

    wtf = random.choice(self.messages)
    await utils.answer(message, self.strings("wait"))
    sleep(2)
    await utils.answer(message, wtf)
