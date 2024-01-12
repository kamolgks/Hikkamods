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

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/Hw_age_ur.png
# meta banner: https://raw.githubusercontent.com/kamolgks/assets/main/Hw_age_ur.jpg

# meta developer: @shitmodules

import datetime

from .. import loader, utils # type: ignore
from hikkatl.types import Message # type: ignore


@loader.tds
class Hw_age_ur(loader.Module):
    """
    Using this module, you can find out the age of a person on the date of his birth.
    """

    strings = {
        "name": "How old are you?",
        "no_date": (
            "<emoji document_id=5447644880824181073>⚠️</emoji>"
            "<b>Enter your date of birth as shown in the example.</b>"
        ),
        "result": (
            "<emoji document_id=5447410659077661506>🌐</emoji>"
            "<b>You (he, she) are <u>{}</u> years old.</b>"
        ),
    }

    strings_ru = {
        "no_date": (
            "<emoji document_id=5447644880824181073>⚠️</emoji>"
            "<b>Введи дату рождения как указано в примере.</b>"
        ),
        "result": (
            "<emoji document_id=5447410659077661506>🌐</emoji>"
            "<b>Тебе (ему, ей) <u>{}</u> лет.</b>"
        ),
    }

    @loader.command(ru_doc="> .yo 01.05.1996 | => (число, месяц, год)")
    async def yo(self, message: Message):
        """> .yo 01.05.1996 | => date, month, year"""
        args = utils.get_args_raw(message)
        try:
            birth_date = datetime.datetime.strptime(args, "%d.%m.%Y").date()
        except ValueError:
            await utils.answer(message, self.strings["no_date"])
            return

        today_date = datetime.date.today()
        age_years = today_date.year - birth_date.year - ((today_date.month, today_date.day) < (birth_date.month, birth_date.day))

        await utils.answer(message, self.strings["result"].format(age_years))
