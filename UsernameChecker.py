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

# meta banner: https://0x0.st/Hi9j.gif.mp4
# meta developer: @shitmodules 

import logging

from telethon import functions
from telethon.tl.types import Message # type: ignore

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class UsernameCheckerMod(loader.Module):
  """
  A module for checking the user for availability.
  Accepted characters: A-z (case-insensitive), 0-9 and underscores.
  Length: 6-32 characters.
  """
  
  strings = {
    "name": "UsernameChecker",
    "author": "shitmodules",
    "true": (
      "<emoji document_id=5215538598970929961>👌</emoji><i><b>User is free and can be used.</b></i>"
    ),
    "wah_args": (
      "<emoji document_id=5359839982468996640>🦆</emoji>There are no arguments or they are not enough. "
      "Example of using this module: <code>.ucheck picdez</code> [The user must be no shorter than 6 letters]"
    ),
    "false": (
      "<emoji document_id=5854973145315806460>👮‍♂️</emoji><i><b>The user is already taken by another user, create a new one for yourself.</b></i>"
    ),
  }

  strings_ru = {
    "true": (
      "<emoji document_id=5215538598970929961>👌</emoji><i><b>Юзер свободен и может быть использован.</b></i>"
    ),
    "wah_args": (
      "<emoji document_id=5359839982468996640>🦆</emoji>Аргументов нет или их недостаточно. "
      "Пример использования этого модуля: <code>.ucheck picdez</code> [Имя пользователя должно быть не короче 6 букв]"
    ),
    "false": (
      "<emoji document_id=5854973145315806460>👮‍♂️</emoji><i><b>Юзер уже занят другим пользователем, придумайте себе новый.</b></i>"
    ),
  }

  @loader.command(ru_doc="> Введите юзер для проверки.")
  async def ucheckcmd(self, message: Message):
    """> Enter the user for verification"""
    args = utils.get_args_raw(message)
    result = await message.client(functions.account.CheckUsernameRequest(username=args))

    if args == "":
      return await utils.answer(message, self.strings("wah_args"))

    if result == True:
      return await utils.answer(message, self.strings("true"))
 
    if result == False:
      return await utils.answer(message, self.strings("false"))
