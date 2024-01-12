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

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/Holiday.png
# meta banner: https://raw.githubusercontent.com/kamolgks/assets/main/Holiday.jpg

# meta developer: @shitmodules

import requests
import logging
import datetime

from .. import loader, utils # type: ignore
from hikkatl.types import Message # type: ignore

logging = logging.getLogger(__name__)

@loader.tds
class Holiday(loader.Module):
    """
    The module checks whether today is a holiday in your region.
    """

    strings = {
        "name": "Holiday",
        "_cfg_doc_country": "Enter your region",
        "nocountry": (
            "<emoji document_id=5269478302967405465>🥰</emoji>"
            "Specify the country in the module config using the <code>{}config Holiday</code>\n\n"
            "<emoji document_id=5443038326535759644>💬</emoji>"
            "You can find your region on the website: {}"
        ),
        "noholiday": (
            "<emoji document_id=5210952531676504517>❌</emoji>"
            "<b>Today is not a <u>holiday.</u></b>"
        ),
        "result": (
            "<emoji document_id=5273951919428084009>✅</emoji>"
            "<b>Todat is <u>{}!</u></b>"
        ),
    }

    strings_ru = {
        "_cfg_doc_country": "Введите свой регион",
        "nocountry": (
            "<emoji document_id=5269478302967405465>🥰</emoji>"
            "Укажите страну в конфиге модуля, используя <code>{}config Holiday</code>\n\n"
            "<emoji document_id=5443038326535759644>💬</emoji>"
            "Вы можете найти свой регион на сайте: {}"
        ),
        "noholiday": (
            "<emoji document_id=5210952531676504517>❌</emoji>"
            "<b>Сегодня не <u>праздник.</u></b>"
        ),
        "result": (
            "<emoji document_id=5273951919428084009>✅</emoji>"
            "<b>Todat is <u>{}!</u></b>"
        ),
    }

    strings_de = {
        "_cfg_doc_country": "Geben Sie Ihre Region ein",
        "nocountry": (
            "<emoji document_id=5269478302967405465>🥰</emoji>"
            "Geben Sie das Land in der Modulkonfiguration mit <code>{}config Holiday</code> an\n\n"
            "<emoji document_id=5443038326535759644>💬</emoji>"
            "Ihre Region finden Sie auf der Website: {}"
        ),
        "noholiday": (
            "<emoji document_id=5210952531676504517>❌</emoji>"
            "<b>Heute ist kein <u>Feiertag.</u></b>"
        ),
        "result": (
            "<emoji document_id=5273951919428084009>✅</emoji>"
            "<b>Todat is <u>{}!</u></b>"
        ),
    }

    strings_uz = {
        "_cfg_doc_country": "Hududingizni kiriting",
        "nocountry": (
            "<emoji document_id=5269478302967405465>🥰</emoji>"
            "<code>{}config Holiday</code> yordamida modul konfigida mamlakatni belgilang\n\n"
            "<emoji document_id=5443038326535759644>💬</emoji>"
            "Siz o'z mintaqangizni veb-saytda topishingiz mumkin: {}"
        ),
        "noholiday": (
            "<emoji document_id=5210952531676504517>❌</emoji>"
            "<b>Bugun <u>bayram</u> emas.</b>"
        ),
        "result": (
            "<emoji document_id=5273951919428084009>✅</emoji>"
            "<b>Todat is <u>{}!</u></b>"
        ),
    }

    def __init__(self):
        self.name = self.strings["name"]
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "country",
                None,
                lambda: self.strings["_cfg_doc_country"],
            ),
        )

    @loader.command(
        ru_doc="> Проверяет, является ли сегодняшний день праздником.",
        de_doc="> Überprüft, ob heute ein Feiertag ist.",
        uz_doc="> Bugun bayram ekanligini tekshiradi.",
    )
    async def holidaycmd(self, message: Message):
        """> Checks if today is a holiday."""
        today = datetime.date.today()
        try:
            url = "https://calendarific.com/supported-countries"
            country = self.config["country"]
            if not country:
                return await utils.answer(message, self.strings["nocountry"].format(self.get_prefix(), url))

            data = (await utils.run_sync(requests.get, f"https://calendarific.com/api/v2/holidays?api_key=3381856f5d6de11793562e3463c231b0a129d48d&country={country}&year={today.year}&month={today.month}&day={today.day}")).json()
            if data.get("response"):
                holidays = data["response"].get("holidays")
                if holidays:
                    holiday_name = holidays[0].get("name")
                    await utils.answer(message, self.strings["result"].format(holiday_name))
                else:
                    await utils.answer(message, self.strings["noholiday"])

        except requests.exceptions.RequestException as e:
            await utils.answer(message, "<b>❌An error occurred while requesting the API: <u>{}</u></b>".format(e))

        except (KeyError, IndexError) as e:
            await utils.answer(message, "<b>❌Failed to get holiday data: <u>{}</u></b>".format(e))
