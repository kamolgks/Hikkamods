#   █▀▀▀█  █▀▄▀█ 
#   ▀▀▀▄▄  █ ▀ █  (shit mods)
#   █▄▄▄█  █   █
#
#            © Copyright 2022
#
#          https://t.me/shitmodules
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: hikka_only
# scope: hikka_min 1.6.0
# meta pic: 
# meta banner: https://x0.at/qGYX.gif
# meta developer: @shitmodules

from .. import loader, utils
from telethon.tl.types import Message
import random
from time import sleep

chat = "prfhgd"

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

  setlang_tr = {
    "wait": "<emoji document_id=5213452215527677338>⏳</emoji><b>Yükleniyor...</b>",
  }

  strings_hi = {
    "wait": "<emoji document_id=5213452215527677338>⏳</emoji><b>लोड हो रहा है । ..</b>",
  }

  strings_uz = {
    "wait": "<emoji document_id=5213452215527677338>⏳</emoji><b>Yuklanmoqda...</b>",
  }

  setlang_de = {
    "wait": "<emoji document_id=5213452215527677338>⏳</emoji><b>Laden...</b>",
  }

  async def client_ready(self, client, db):
        self.db = db
        self.client = client
        post = (await client.get_messages("shitmodules", ids=831))
        await post.react("❤️")

  async def client_ready(self):
        self.messages = await self.client.get_messages(chat, limit=None)
  
  @loader.command(ru_doc="Самые высокооплачиваемые профессии в мире")
  async def profscmd(self, message: Message):
    """.profs The highest paid professions in the world"""
    wtf = random.choice(self.messages)
    await utils.answer(message, self.strings("wait"))
    sleep(2)
    await utils.answer(
      message, 
      wtf,
      )
