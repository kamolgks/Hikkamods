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

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/IndividualLinks.jpg
# meta banner: https://te.legra.ph/file/a68d6b0715e417b619f78.mp4
# meta developer: @shitmodules

import logging

from .. import loader, utils
from telethon.tl.types import Message
from telethon.tl.functions.channels import JoinChannelRequest

logger = logging.getLogger(__name__)

@loader.tds
class IndividualLinks(loader.Module):
  """Links to individual content in telegram (18+) Use at your own risk"""
  
  strings = {
    "name": "IndividualLinks",
    "author": "shitmodules",
    "processing": (
      "<emoji document_id=5213452215527677338>⏳</emoji><i><b>Loading...</b></i>"
    ),
    "links": (
      "<emoji document_id=5357369611769619859>🦆</emoji><i><b>To view content, use numbers with access to 18+ content (I recommend USA)\n<emoji document_id=5395689060876426750>😇</emoji>Use <code>.list</code> to see the list of countries where 18+ content in tg is </b></i>\n\n"
      "https://t.me/+YJXUGPO--KU2YzBi\n\n"
      "===========================\n\n"
      "https://t.me/+b3ThTlaz2AczOTZl\n"
      "===========================\n\n"
      "https://t.me/+Ve0XZLOgWg8yODdi\n\n"
      "===========================\n\n"
      "https://t.me/+yegz2e53-bFmZjIy\n\n"
      "===========================\n\n"
      "https://t.me/+RfdHbMqqeUdiNDUy\n\n"
      "===========================\n\n"
      "https://t.me/+1Us4Bg6rR3hjZjFl\n\n"
      "===========================\n\n"
      "https://t.me/+scyfvcZMh1YyOWIy\n\n"
      "===========================\n\n"
      "https://t.me/+EjMIiaCIDzZlMzA6\n\n"
      "===========================\n\n"
      "https://t.me/+GjlIs_gIxexiNzgy\n\n"
      "===========================\n\n"
      "https://t.me/+ISFyMTT7TJJjODNi\n\n"
    ),
    "links_open": (
      "<i><b><emoji document_id=5357369611769619859>🦆</emoji>Links for bodies who have unavailable 18+ content (photos)</b></i>\n\n"
      "https://t.me/+4Cbqczaexc8xMGJi\n"
      "https://t.me/+TfSJi7Xg6SNlZGJi\n"
      "https://t.me/+jJlbvbnMQHJiYzBi\n"
      "https://t.me/+-OsCW3qLfiVjMGVi\n"
      "https://t.me/+HUuBDnMf3utkYTIy\n"
      "https://t.me/+eu8omMCpks1kNjIy\n"
    ),
    "list": (
      "<i><b><emoji document_id=5866355487255039002>🚀</emoji>There is no single official list of countries that support pornographic content on telegram. However, many countries allow users to view and share pornographic content on telegram. This includes the following countries:\n<emoji document_id=5215203655946346044>🔞</emoji>The information may be incorrect, it is taken from the Internet</i>\n\n- Russia (RU)\n- USA (US)\n- Canada (CA)\n- Australia (AU)\n- Ireland (IE)\n- Netherlands (NL)\n- France (FR)\n- Great Britain (GB)\n- Spain (ES)\n- Germany (DE)\n- Italy (IT)\n- Sweden (SE)\n- Norway (NO)\n- Denmark (DK)\n- Japan (JP)</b>"
    ),
  }
  
  strings_ru = {
    "processing": (
      "<emoji document_id=5213452215527677338>⏳</emoji><i><b>Загрузка...</b></i>"
    ),
    "links": (
      "<emoji document_id=5357369611769619859>🦆</emoji><i><b>Для просмотра контента используйте номера с доступом к контенту 18+ (рекомендую США)\n<emoji document_id=5395689060876426750>😇</emoji>Используйте <code>.list</code> чтобы увидеть список стран где нету ограничений на 18+ контент в телеграмме</b></i>\n\n"
      "https://t.me/+YJXUGPO--KU2YzBi\n\n"
      "===========================\n\n"
      "https://t.me/+b3ThTlaz2AczOTZl\n\n"
      "===========================\n\n"
      "https://t.me/+Ve0XZLOgWg8yODdi\n\n"
      "===========================\n\n"
      "https://t.me/+yegz2e53-bFmZjIy\n\n"
      "===========================\n\n"
      "https://t.me/+RfdHbMqqeUdiNDUy\n\n"
      "===========================\n\n"
      "https://t.me/+1Us4Bg6rR3hjZjFl\n\n"
      "===========================\n\n"
      "https://t.me/+scyfvcZMh1YyOWIy\n\n"
      "===========================\n\n"
      "https://t.me/+EjMIiaCIDzZlMzA6\n\n"
      "===========================\n\n"
      "https://t.me/+GjlIs_gIxexiNzgy\n\n"
      "===========================\n\n"
      "https://t.me/+ISFyMTT7TJJjODNi\n\n"
    ),
    "links_open": (
      "<i><b><emoji document_id=5357369611769619859>🦆</emoji>Ссылки для тел, у которых недоступен контент 18+ (фотки)</b></i>\n\n"
      "https://t.me/+4Cbqczaexc8xMGJi\n"
      "https://t.me/+TfSJi7Xg6SNlZGJi\n"
      "https://t.me/+jJlbvbnMQHJiYzBi\n"
      "https://t.me/+-OsCW3qLfiVjMGVi\n"
      "https://t.me/+HUuBDnMf3utkYTIy\n"
      "https://t.me/+eu8omMCpks1kNjIy\n"
    ),
    "list": (
      "<i><b><emoji document_id=5866355487255039002>🚀</emoji>Единого официального списка стран, поддерживающих порнографический контент в Telegram, не существует. Однако многие страны разрешают пользователям просматривать и делиться порнографическим контентом в Telegram. Сюда входят  следующие страны:\n<emoji document_id=5215203655946346044>🔞</emoji>Информация может быть неверной, она взята с интернета</i>\n\n- Россия (RU)\n- США (US)\n- Канада (CA)\n- Австралия (AU)\n- Ирландия (IE)\n- Нидерланды (NL)\n- Франция (FR)\n- Великобритания (GB)\n- Испания (ES)\n- Германия (DE)\n- Италия (IT)\n- Швеция (SE)\n- Норвегия (NO)\n- Дания (DK)\n- Япония (JP)</b>"
    ),
  }
  
  async def client_ready(self, client, db):
    self.db = db
    self.client = client
    post = (await client.get_messages("shitmodules", ids=32))
    await post.react("❤️")
    await client(JoinChannelRequest(channel=self.strings("author")))
  
  @loader.command(ru_doc="Ссылки на индивидуальный контент в телеграмме (18+)", only_pm=True)
  async def contprncmd(self, message: Message):
    """Links to individual content in telegram (18+)"""
    await utils.answer(message, self.strings("processing"))
    await utils.answer(message, self.strings("links", message))
    
  @loader.command(ru_doc="Ссылки для тел у кого недоступен 18+контент (Фотки {нюдсы} и возможно видосы) ", only_pm=True)
  async def kopen(self, message: Message):
    """Links for bodies who have unavailable 18+ content (photos and maybe videos)"""
    await utils.answer(message, self.strings("processing"))
    await utils.answer(message, self.strings("links_open", message))
      
  @loader.command(ru_doc="Список стран поддерживающие 18+ контент в телеграмме (информация может быть неточной)", only_pm=True)
  async def list(self, message: Message):
    """Opens a list of numbers supporting 18+ content"""
    await utils.answer(message, self.strings("processing"))
    await utils.answer(message, self.strings("list"))
