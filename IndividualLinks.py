__version__ = (0, 0, 3)
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

logger = logging.getLogger(__name__)

@loader.tds
class IndividualLinksMod(loader.Module):
  """
  🈂️Links to individual content in telegram. Use at your own risk
  ⛔Do not try to use this module in groups, it only works in PM
  """
  
  strings = {
    "name": "IndividualLinks",
    "author": "shitmodules",
    "processing": (
      "<emoji document_id=5213452215527677338>⏳</emoji><b>Loading...</b>"
    ),
    "links": (
      "<emoji document_id=5357369611769619859>🦆</emoji>\n\n"
      "https://t.me/+YJXUGPO--KU2YzBi\n"
      "https://t.me/+b3ThTlaz2AczOTZl\n"
      "https://t.me/+Ve0XZLOgWg8yODdi\n"
      "https://t.me/+yegz2e53-bFmZjIy\n"
      "https://t.me/+RfdHbMqqeUdiNDUy\n"
      "https://t.me/+1Us4Bg6rR3hjZjFl\n"
      "https://t.me/+scyfvcZMh1YyOWIy\n"
      "https://t.me/+EjMIiaCIDzZlMzA6\n"
      "https://t.me/+GjlIs_gIxexiNzgy\n"
      "https://t.me/+ISFyMTT7TJJjODNi\n"
      "https://t.me/+DRZurxHB_EVkMjZi\n"
      "https://t.me/+to8L5hJ3LJ8xYzlk\n"
    ),

    "links_open": (
      "<b><emoji document_id=5357369611769619859>🦆</emoji>"
      "Links for bodies with channels unavailable</b>\n\n"
      "https://t.me/+4Cbqczaexc8xMGJi\n"
      "https://t.me/+TfSJi7Xg6SNlZGJi\n"
      "https://t.me/+jJlbvbnMQHJiYzBi\n"
      "https://t.me/+-OsCW3qLfiVjMGVi\n"
      "https://t.me/+HUuBDnMf3utkYTIy\n"
      "https://t.me/+eu8omMCpks1kNjIy\n"
      "https://t.me/+ibZzteZEQ_gwYjIy\n"
    )
  }

  strings_ru = {
    "processing": (
      "<emoji document_id=5213452215527677338>⏳</emoji><i><b>Загрузка...</b></i>"
    ),
    "links": (
      "<emoji document_id=5357369611769619859>🦆</emoji>\n\n"
      "https://t.me/+YJXUGPO--KU2YzBi\n"
      "https://t.me/+b3ThTlaz2AczOTZl\n"
      "https://t.me/+Ve0XZLOgWg8yODdi\n"
      "https://t.me/+yegz2e53-bFmZjIy\n"
      "https://t.me/+RfdHbMqqeUdiNDUy\n"
      "https://t.me/+1Us4Bg6rR3hjZjFl\n"
      "https://t.me/+scyfvcZMh1YyOWIy\n"
      "https://t.me/+EjMIiaCIDzZlMzA6\n"
      "https://t.me/+GjlIs_gIxexiNzgy\n"
      "https://t.me/+ISFyMTT7TJJjODNi\n"
      "https://t.me/+DRZurxHB_EVkMjZi\n"
      "https://t.me/+cVTQPAPGh40wNjVi\n"
    ),
    "links_open": (
      "<b><emoji document_id=5357369611769619859>🦆</emoji>"
      "Ссылки для тел у которых недоступны каналы</b>\n\n"
      "https://t.me/+4Cbqczaexc8xMGJi\n"
      "https://t.me/+TfSJi7Xg6SNlZGJi\n"
      "https://t.me/+jJlbvbnMQHJiYzBi\n"
      "https://t.me/+-OsCW3qLfiVjMGVi\n"
      "https://t.me/+HUuBDnMf3utkYTIy\n"
      "https://t.me/+eu8omMCpks1mjIy\n"
      "https://t.me/+ibZzteZEQ_gwYjIy\n"
    )
  }

  @loader.command(ru_doc="Ссылки на те самые сурсы", only_pm=True)
  async def chnlcmd(self, message: Message):
    """Links to individual content in telegram"""
    await utils.answer(message, self.strings("processing"))
    await utils.answer(message, self.strings("links", message))

  @loader.command(ru_doc="Фотки и возможно видосы", only_pm=True)
  async def wahcmd(self, message: Message):
    """photos and maybe videos"""
    await utils.answer(message, self.strings("processing"))
    await utils.answer(message, self.strings("links_open", message))
