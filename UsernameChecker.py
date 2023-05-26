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

# meta banner: https://raw.githubusercontent.com/kamolgks/assets/main/UsernameChecker.jpg

# meta developer: @shitmodules

import logging

from telethon import functions
from telethon.tl.types import Message

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
        "true": (
            "<emoji document_id=5215538598970929961>👌</emoji><i><b>User is free and can be used.</b></i>"
        ),
        "wah_args": (
            "<emoji document_id=5359839982468996640>🦆</emoji>There are no arguments or they are not enough. "
            "Example of using this module: <code>.ucheck picdato</code> [The user must be no shorter than 6 letters]"
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
            "Пример использования этого модуля: <code>.ucheck pizdato</code> [Имя пользователя должно быть не короче 6 букв]"
        ),
        "false": (
            "<emoji document_id=5854973145315806460>👮‍♂️</emoji><i><b>Юзер уже занят другим пользователем, придумайте себе новый.</b></i>"
        ),
    }

    @loader.command(
        ru_doc="> Введите юзер для проверки.",
    )
    async def ucheckcmd(self, message: Message):
        """> Enter the user for verification"""
        args = utils.get_args_raw(message)
        result = await message.client(functions.account.CheckUsernameRequest(username=args))

        if args == "":
            await utils.answer(message, self.strings("wah_args"))
            return

        if result == True:
            await utils.answer(message, self.strings("true"))
            return

        if result == False:
            await utils.answer(message, self.strings("false"))
            return
