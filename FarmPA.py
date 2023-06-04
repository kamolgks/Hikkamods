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

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/FarmPA.jpg
# meta banner: https://raw.githubusercontent.com/kamolgks/assets/main/FarmPA.jpeg

# meta developer: @shitmodules

import logging
import asyncio

from telethon.tl.types import Message
from .. import loader, utils

logging = logging.getLogger("FarmPA")


@loader.tds
class FarmPAMod(loader.Module):
    """
    Module for automatic farming sm in Pipisa bot | PA -> PipisaBot by shitmodules.t.me
    """

    strings = {
        "name": "FarmPA",
        "group_id": "Group ID",
        "enable": "<b>FarmPA successfully launched</b>",
        "disable": "<b>FarmPA successfully stopped</b>",
        "loading": "<b>Loading...</b>",
        "id_error": "<b>No group id for farming. Use: </b><code>.config FarmPA</code> <b>to enter group id.</b>",
    }

    strings_ru = {
        "group_id": "Айди группы",
        "enable": "<b>FarmPA успешно запущен</b>",
        "disable": "<b>FarmPA успешно остановлен</b>",
        "loading": "<b>Загрузка...</b>",
        "id_error": "<b>Не указан айди группы для фарма. Используй: </b><code>.config FarmPA</code> <b>для ввода ийди группы.</b>",
    }

    strings_uz = {
        "group_id": "Guruh ID-si",
        "enable": "<b>FarmPA muvaffaqiyatli ishga tushirildi</b>",
        "disable": "<b>FarmPA muvaffaqiyatli to'xtatildi</b>",
        "loading": "<b>Yuklanmoqda...</b>",
        "id_error": "<b>Dehqonchilik uchun guruh identifikatori yo'q. Guruh identifikatorini kiritish uchun </b><code>.config FarmPA</code> <b>dan foydalaning.</b>",
    }

    strings_de = {
        "group_id": "Gruppen-ID",
        "enable": "<b>FarmPA erfolgreich gestartet</b>",
        "disable": "<b>FarmPA erfolgreich deaktiviert</b>",
        "loading": "<b>Laden...</b>",
        "id_error": "<b>Es gibt keine Gruppen-ID für die Landwirtschaft. Verwenden Sie </b><code>.config FarmPA</code> <b>, um eine Gruppen-ID einzugeben.</b>",
    }

    strings_es = {
        "group_id": "Identificación del grupo",
        "enable": "<b>FarmPA se inició correctamente</b>",
        "disable": "<b>FarmPA deshabilitado con éxito</b>",
        "loading": "<b>Cargando...</b>",
        "id_error": "<b>No hay ID de grupo para la agricultura. Usa </b><code>.config FarmPA</code> <b> para ingresar una ID de grupo.</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "group_id",
                None,
                lambda: self.strings["group_id"],
            ),
        )

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    @loader.command(
        ru_doc="Включить/отключить режим автоматического фарма для бота Pipisa.",
        uz_doc="Pipisa boti uchun avtomatik dehqonchilik rejimini yoqadi/o‘chiradi.",
        de_doc="Aktiviert/deaktiviert den Auto-Farming-Modus für den Pipisa-Bot.",
        es_doc="Habilita/deshabilita el modo de cultivo automático para el bot Pipisa.",
    )
    async def dfarm(self, message: Message):
        """
        Turns on/off automatic farming mode for the Pipisa bot.
        """
        try:
            status = self.db.get("farm_status", "status")
            msg = await utils.answer(message, self.strings["loading"])
            text = "/dick"
            group_id = self.config["group_id"]
            if not group_id:
                await msg.edit(self.strings["id_error"])
                return

            if status:
                self.db.set("farm_status", "status", False)
                await utils.answer(message, self.strings["disable"])

            else:
                self.db.set("farm_status", "status", True)
                await utils.answer(message, self.strings["enable"])
                while self.db.get("farm_status", "status"):
                    await message.client.send_message(int(group_id), text)
                    await asyncio.sleep(84600)

        except Exception as e:
            await utils.answer(message, f"Something went wrong..\nError: {e}\n\nIf the error persists, please report this error in the support chat: https://t.me/shitmodules_chat")
            logging.info("An error has occurred")

    @loader.command(
        ru_doc="Команда .chatid показывает идентификатор чата.",
        uz_doc=".chatid buyrug'i suhbat identifikatorini ko'rsatadi.",
        de_doc="Der Befehl .chatid zeigt die Chat-ID an.",
        es_doc="El comando .chatid muestra la identificación del chat.",
    )
    async def chatidcmd(self, message):
        """The .chatid command shows the chat ID."""
        if message.is_private:
            await message.edit("<b>This is not a chat!</b>")
            return

        args = utils.get_args_raw(message)
        to_chat = None

        try:
            if args:
                to_chat = int(args) if args.isdigit() else args
            else:
                to_chat = message.chat_id

        except ValueError:
            to_chat = message.chat_id

        chat = await message.client.get_entity(to_chat)

        await message.edit(
            f"<b>ID</b>: <code>{chat.id}</code>"
        )
