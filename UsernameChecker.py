__version__ = (1, 0, 2)
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

from .. import loader, utils # type: ignore

from telethon.tl.types import Message
from telethon.tl.functions.account import CheckUsernameRequest

logger = logging.getLogger(__name__)


@loader.tds
class UsernameChecker(loader.Module):
    """
    Validates a username and checks availability.

    Accepted characters: A-z (case-insensitive), 0-9 and underscores.
    Length: 5-32 characters.
    """

    strings = {
        "name": "UsernameChecker",
        "true": (
            "<emoji document_id=5215538598970929961>👌</emoji><i><b>User <u>{}</u> is free and can be used.</b></i>"
        ),
        "noargs": (
            "<emoji document_id=5359839982468996640>🦆</emoji>"
            "There are no arguments or they are not enough. Example of using this module: "
            "<code>.ucheck myusername</code> (The user must be no shorter than 6 letters)"
        ),
        "false": (
            "<emoji document_id=5854973145315806460>👮‍♂️</emoji>"
            "<i><b>The user <u>{}</u> is already taken by another user, create a new one for yourself.</b></i>"
        ),
        "error": (
            "<emoji document_id=5210952531676504517>❌</emoji>"
            "An error occurred while executing the request: {}"
        ),
    }

    strings_ru = {
        "true": (
            "<emoji document_id=5215538598970929961>👌</emoji><i><b>Юзер <u>{}</u> свободен и может быть использован.</b></i>"
        ),
        "noargs": (
            "<emoji document_id=5359839982468996640>🦆</emoji>"
            "Аргументов нет или их недостаточно. Пример использования этого модуля: "
            "<code>.ucheck musername</code> (Имя пользователя должно быть не короче 6 букв)"
        ),
        "false": (
            "<emoji document_id=5854973145315806460>👮‍♂️</emoji>"
            "<i><b>Юзер <u>{}</u> уже занят другим пользователем, придумайте себе новый.</b></i>"
        ),
        "error": (
            "<emoji document_id=5210952531676504517>❌</emoji>"
            "❌ Произошла ошибка при выполнении запроса: {}"
        ),
    }

    def __init__(self):
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

    @loader.command(ru_doc="> Введите юзер для проверки.")
    async def ucheck(self, message: Message):
        """> Enter the user for verification"""
        args = utils.get_args_raw(message)
        if not args:
            return await utils.answer(message, self.strings["noargs"])

        try:
            result = await message.client(CheckUsernameRequest(username=args)) # type: ignore
            if result:
                return await utils.answer(message, self.strings["true"].format(args))
            else:
                return await utils.answer(message, self.strings["false"].format(args))
        except Exception as e:
            return await utils.answer(message, self.strings["error"].format(e))
