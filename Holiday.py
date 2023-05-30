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

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/Holiday.png
# meta banner: https://raw.githubusercontent.com/kamolgks/assets/main/Holiday.jpg

# meta developer: @shitmodules

import requests
import logging
import datetime

from telethon.tl.types import Message

from .. import loader, utils

logging = logging.getLogger("HolidayMod")


@loader.tds
class HolidayMod(loader.Module):
    """The module checks whether today is a holiday in your region."""

    strings = {
        "name": "Holiday",
        "api_key_doc": "API key for Holiday",
        "country_doc": "Enter your region",
        "countries": "<b>A list of all supported countries can be found here - </b>",
        "no_api_key": "<b>The <u>API key</u> was not found, or you did not specify your region in the module config. You can get the API key on the website [https://calendarific.com ] and enter the key or region in <code>.config Holiday</code></b>"
    }

    strings_ru = {
        "api_key_doc": "API ключ для Holiday",
        "country_doc": "Введите свой регион",
        "countries": "<b>Список всех поддерживаемых стран находится здесь - </b>",
        "no_api_key": "<b>Не найден <u>API-ключ</u>, либо вы не указали свой регион в конфиге модуля. Получить ключ API можно на сайте [https://calendarific.com ] и ввести ключ или регион в <code>.config Holiday</code></b>",
    }

    strings_de = {
        "api_key_doc": "API-Schlüssel für Feiertag",
        "country_doc": "Geben Sie Ihre Region ein",
        "countries": "<b>Liste aller unterstützten Länder ist hier - </b>",
        "no_api_key": "<b><u>API-Schlüssel</u> nicht gefunden, oder Sie haben Ihre Region nicht in der Modulkonfiguration angegeben. Sie können einen API-Schlüssel auf der Website [https://calendarific.com] erhalten ] und geben Sie den Schlüssel oder die Region in <code>.config Holiday</code></b> ein",
    }

    strings_uz = {
        "api_key_doc": "Bayram uchun API kaliti",
        "country_doc": "Hududingizni kiriting",
        "countries": "<b>Qo'llab-quvvatlanadigan barcha mamlakatlar ro'yxati bu yerda - </b>",
        "no_api_key": "<b><u>API kaliti</u> topilmadi yoki modul konfiguratsiyasida mintaqangizni ko‘rsatmadingiz. API kalitini [https://calendarific.com” veb-saytidan olishingiz mumkin. ] va kalit yoki mintaqani <code>.config Holiday</code></b>-ga kiriting",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "api_key",
                None,
                lambda: self.strings["api_key_doc"],
                validator=loader.validators.Hidden(loader.validators.String()),
            ),
            loader.ConfigValue(
                "country",
                None,
                lambda: self.strings["country_doc"],
            ),
        )

    @loader.command(
        ru_doc="> Проверяет, является ли сегодня праздником, и отображает информацию об этом празднике",
        de_doc="> Überprüft, ob heute ein Feiertag ist und zeigt Informationen zu diesem Feiertag an",
        uz_doc="> Bugun bayram ekanligini tekshiradi va ushbu bayram haqidagi ma'lumotlarni ko'rsatadi",
    )
    async def holidaycmd(self, message: Message):
        """> Checks if today is a holiday and displays information about it"""
        today = datetime.date.today()

        try:
            api_key = self.config["api_key"]
            country = self.config["country"]
            if not api_key or not country:
                await utils.answer(
                    message,
                    self.strings["no_api_key"],
                )
                return

            response = requests.get(
                f"https://calendarific.com/api/v2/holidays?api_key={api_key}&country={country}&year={today.year}&month={today.month}&day={today.day}",
            )
            response.raise_for_status()
            rj = response.json()
            holidays = rj.get("response").get("holidays")
            if holidays:
                holiday_name = holidays[0].get("name")
                await utils.answer(message, f"🥳<b>Todat is <u>{holiday_name}!</u></b>")
                logging.INFO("🥳Сongratulations!")
            else:
                await utils.answer(message, "<b>❌Today is not a <u>holiday.</u></b>")

        except requests.exceptions.RequestException as e:
            await utils.answer(message, "<b>❌An error occurred while requesting the API: <u>{}</u></b>".format(e))

        except (KeyError, IndexError) as e:
            await utils.answer(message, "<b>❌Failed to get holiday data: <u>{}</u></b>".format(e))

    @loader.command(
        ru_doc="> Поддерживаемые регионы",
        de_doc="> Unterstützte Regionen",
        uz_doc="> Qo'llab-quvvatlanadigan hududlar",
    )
    async def countriescmd(self, message: Message):
        """> Supported regions"""
        link = "https://calendarific.com/supported-countries"
        await utils.answer(
            message,
            self.strings("countries") + link,
        )
