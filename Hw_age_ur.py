__version__ = (1, 0, 0)
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

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/Hw_age_ur.png
# meta banner: https://raw.githubusercontent.com/kamolgks/assets/main/Hw_age_ur.jpg

# meta developer: @shitmodules

import datetime

from .. import loader, utils

from telethon.tl.types import Message


@loader.tds
class Hw_age_ur(loader.Module):
    """
    Using this module, you can find out the age of a person on the date of his birth.
    """

    strings = {
        "name": "Hw_age_ur?",
        "no_date": "❗️<b>Enter your date of birth as shown in the example.</b>",
    }

    strings_ru = {
        "no_date": "❗️<b>Введи дату рождения как указано в примере.</b>",
    }

    @loader.command()
    async def fy(self, message: Message):
        """> Usage example: .yo 01.05.1996 | => date, month, year"""

        args = utils.get_args_raw(message)

        if not args:
            await utils.answer(
                message,
                self.strings["no_date"],
            )
            return

        birth_date = datetime.datetime.strptime(args, "%d.%m.%Y").date()
        today_date = datetime.date.today()

        age_years = today_date.year - birth_date.year

        if today_date.month < birth_date.month or (
            today_date.month == birth_date.month and today_date.day < birth_date.day,
        ):
            age_years -= 1

        await message.edit(f"😼<b>You [he, she] are <u>{age_years}</u> years old.</b>")
