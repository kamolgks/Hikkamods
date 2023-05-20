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

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/RandomChats.jpg
# meta banner: http://devs.farkhodovme.tk/bannerget/kamolgks/randomchats.png

# meta developer: @shitmodules

from telethon import events, functions

from telethon.tl.types import Message
from asyncio.exceptions import TimeoutError
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import loader, utils


@loader.tds
class RandomChatsMod(loader.Module):
    """The module throws off a random chat"""

    strings = {
        "name": "RandomChats",
        "processing": "<emoji document_id=5190568934717270805>🙂</emoji><b>Uploading a chat...</b>",
        "un-iris": (
            "<emoji document_id=5280821895711697516>⛔️</emoji>"
            "<b>Unlock this bot: @iris_moon_bot</b>",
        ),
        "time-err": (
            "<emoji document_id=5280821895711697516>⛔️</emoji><b>The waiting time has expired.</b> "
            "<b>Either the bot is loaded, or it's dead. Try again a little later</b>"
        ),
    }

    strings_ru = {
        "processing": "<emoji document_id=5190568934717270805>🙂</emoji><b>Загрузка чата...</b>",
        "un-iris": (
            "<emoji document_id=5280821895711697516>⛔️</emoji>"
            "<b>Разблокируй этого бота: @iris_moon_bot</b>",
        ),
        "time-err": (
            "<emoji document_id=5280821895711697516>⛔️</emoji><b>Истекло время ожидания.</b> "
            "<b>Либо бот нагружен, либо он умер. Попробуйте немного позже.</b>"
        ),
    }

    strings_uz = {
        "processing": "<emoji document_id=5190568934717270805>🙂</emoji><b>Chat yuklanmoqda...</b>",
        "un-iris": (
            "<emoji document_id=5280821895711697516>⛔️</emoji>"
            "<b>Ushbu botni qora ro'yxatdan chiqaring: @iris_moon_bot</b>",
        ),
        "time-err": (
            "<emoji document_id=5280821895711697516>⛔️</emoji>Kutish vaqti tugadi.</b> "
            "<b>Yoki bot Yuklangan yoki u vafot etgan. Birozdan keyin sinab ko'ring."
        ),
    }

    strings_kk = {
        "processing": "<emoji document_id=5190568934717270805>🙂</emoji><b>Чатты жүктеу...</b>",
        "un-iris": (
            "<emoji document_id=5280821895711697516>⛔️</emoji>"
            "<b>Бұл боттың құлпын ашыңыз: @iris_moon_bot</b>",
        ),
        "time-err": (
            "<emoji document_id=5280821895711697516>⛔️</emoji><b>Күту уақыты аяқталды.</b>"
            "<b>Не бот жүктелген, не ол қайтыс болды. Сәл кейінірек көріңіз.</b>"
        ),
    }

    strings_tr = {
        "processing": "<emoji document_id=5190568934717270805>🙂</emoji><b>Sohbet yükleniyor...</b>",
        "un-iris": (
            "<emoji document_id=5280821895711697516>⛔️</emoji><b> </b>"
            "<b>Bu botun engellemesini kaldırın: @iris_moon_bot</b>"
        ),
        "time-err": (
            "<emoji document_id=5280821895711697516>⛔️</emoji><b>zaman aşımı süresi doldu.</b>"
            "<b>Ya bot yüklendi ya da öldü. Lütfen daha sonra tekrar deneyiniz.</b>"
        ),
    }

    @loader.command(
        ru_doc="> Кидает рандомную ссылку на чат",
        uz_doc="> Tasodifiy chat havolasini tashlaydi",
        kk_doc="> Кездейсоқ чат сілтемесін лақтырады",
        tr_doc="> Sohbete rastgele bir bağlantı atar",
    )
    async def rchatcmd(self, message: Message):
        """> Throws a random link to the chat"""

        msg = await utils.answer(message, self.strings("processing"))
        chat = "@iris_moon_bot"

        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(
                    incoming=True, from_users=chat))
                await message.client.send_message(chat, "🔀 Случайная беседа")
                response = await response
            except YouBlockedUserError:
                await message.edit(self.strings("un-iris"))
                return

            except TimeoutError:
                await utils.answer(message, self.strings("time-err"))
                return

            if response.text:
                await msg.edit(f"<emoji document_id=5190568934717270805>🙂</emoji><b>{response.text}<b>")

            await message.client(
                functions.messages.DeleteHistoryRequest(
                    peer="@iris_moon_bot", max_id=0, just_clear=False, revoke=True,
                ),
            )
