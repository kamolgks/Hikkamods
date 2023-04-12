__version__ = (0, 0, 2)
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

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/GameForAndroid.jpg
# meta banner: https://x0.at/0H0-.gif

# meta developer: @shitmodules

from .. import loader
from hikkatl.types import Message
from ..inline.types import InlineCall

import logging

logger = logging.getLogger(__name__)


@loader.tds
class GamesForAndroidMod(loader.Module):
    """Hacked android games (All in categories, choose what you like and download.)"""

    strings = {
        "name": "GamesForAndroid",
        "categories_list": (
            "<i><b>🙂Here is a list of game categories:\n"
            "Strategy | Online games (multiplayer) | Horror game |\n| "
            "Racing | Arcade | ⚠️ All games and their categories are taken from the Internet.</b></i>"
        ),
        "subway": (
            "Help Jake, Tricky & Fresh escape from the grumpy Inspector and his dog!\n\nDASH as fast as you can!\n\nDODGE the oncoming trains!"
        ),
        "subwaysurf_mod": (
            "Help Jake, Tricky & Fresh escape from the grumpy Inspector and his dog!\n\nDASH as fast as you can!\n\nDODGE the oncoming trains!\n\n"
            "💰 Mod features: Infinite money, keys, hoverboards and boosters\nFree purchases for real money (after the error appears, close the payment window);\n\nyou can jump an infinite number of times."
        ),
        "traffic_rider_org": (
            "🏍️Another masterpiece from the creators of Traffic Racer. This time, you are behind the wheels of a motorbike in a much more detailed gaming experience, but also retaining the old school fun and simplicity."
        ),
        "traffic_rider_mod": (
            "🏍️Another masterpiece from the creators of Traffic Racer. This time you are driving a motorcycle in a much more detailed gameplay, but at the same time you keep the fun and simplicity of the old school.\n\nMods: a lot of money"
        ),
        "fnaf": (
            "🐻Keep an eye on the animatronics and you'll make it thru the night... probably.\n\nNOTE: Remastered version from the PC version. A device with at least 2 GB of RAM is required for this game to run properly."
        ),
        "fnaf_2": (
            "🐻No place to run, and exactly one place to hide.\n\nNOTE: Remastered version from the PC version. A device with at least 2 GB of RAM is required for this game to run properly."
        ),
        "clash_cl": (
            "Epic combat strategy game. Build your village, train your troops & go to battle!\n\nJoin millions of players worldwide as you build your village, raise a clan, and compete in epic Clan Wars!\n\nMustachioed Barbarians, fire wielding Wizards, and other unique troops are waiting for you! Enter the world of Clash!"
        ),
        "clash_r": (
            "Clash Royale is a real-time, head-to-head battle game set in the Clash Universe.\n\nEnter the Arena! Build your Battle Deck and outsmart the enemy in fast real-time battles. From the creators of CLASH OF CLANS comes a real-time multiplayer battle game starring your favourite Clash characters and more. Start battling against players from around the world!"
        ),
        "chess_cl": (
            "Have fun playing the two player and multiplayer puzzle board Chess game!"
        ),
        "stick_war": (
            "Learn the way of the Sword, Spear, Archer, and Mage. Only you can save Inamorta!\n\nOne of the most popular and highest rated web games of all time now comes to mobile!Learn the way of the Sword, Spear, Archer, and Mage. Only you can save Inamorta!\n\nOne of the most popular and highest rated web games of all time now comes to mobile!"
        ),
        "snake_io": (
            "Slither Eat Battle. Play this addicting online & offline arcade snake blast game\n\nSlither through a new competitive version of Snake 🐍 and survive as long as you can! Challenge your friends and try to be the biggest worm in Snake.io!"
        ),
        "durak_online": (
            "Durak online is a Russian card game.\n\nDurak online - the favorite card game.\nThe object of the game is to get rid of all one's cards. At the end of the game, the last player with cards in their hand is referred to as the fool (durak - Дурак)."
        ),
        "granny": (
            "Granny keeps you locked in her house.\n\nWelcome to Granny.\n\nGranny keeps you locked in her house.\nNow you have to try to get out of her house, but be careful and quiet. She hears everything.\nIf you drop something on the floor, she hears it and comes running.\nYou can hide in wardrobes or under beds.\n\nYou have 5 days"
        ),
        "bhop_pro": (
            "You may need to work hard, but you can also be a bhop pro.\n\nYou can jump and bunny hop in fps mode with bhop pro. You can prove that you are really a bhop master with the scores and durations you will get. You must continuously turn right or left and synchronously jump at the same time to be able to do successful bunny hops. Bhop Pro is a portable mobile bhop style jumping game. You can get new rankings by doing parkour quests. If you can really do it, you will be a 'bhop pro'."
        ),
        "bhop_pro_mod": (
            "You may need to work hard, but you can also be a bhop pro.\n\nYou can jump and bunny hop in fps mode with bhop pro. You can prove that you are really a bhop master with the scores and durations you will get. You must continuously turn right or left and synchronously jump at the same time to be able to do successful bunny hops. Bhop Pro is a portable mobile bhop style jumping game. You can get new rankings by doing parkour quests. If you can really do it, you will be a 'bhop pro'.\n\n"
            "[Lots of money] - Counter Strike GO style high jumps"
        ),
        "rider": (
            "Get ready for some flippin' action!\n\nGet ready for some flippin' action!\n\nPerform insane stunts while you cruise through the never-ending world of Rider! Grab your motorcycle and start flipping like a maniac!"
        ),
        "support_chat_btn": "✨ Support Chat",
        "more_modules_btn": "🔥 More Modules",
        "strategy": "<i><b>🫡Strategy games</b></i>",
        "multiplayer": "<i><b>🕳️Here you will find multiplayer games</b></i>",
        "horror": "<i><b>😁Here you will find arcade games</b></i>",
        "racing": "<i><b>🪄Here you will find Racing games</b></i>",
        "arcade": "<i><b>🤭Here you will find arcade games</b></i>",
        "back": "↙️ Back",
        "close": "🔻 Close",
    }

    strings_ru = {
        "categories_list": (
            "<i><b>🙂Вот список категорий игр:\n"
            "Стратегические игры | Онлайн игры (можно играть онлайн (1-1)) | Хоррор игры |\n|"
            "Гоночные игры | Аркады | ⚠️ Все игры и их категории взяты из Интернета.</b></i>"
        ),
        "subway": (
            "Помогите Джейку, Трикки и Фрешу сбежать от сварливого инспектора и его собаки!\n\nМЧИСЬ так быстро, как только можешь!\n\nУВОРАЧИВАЙТЕСЬ от встречных поездов!"
        ),
        "subwaysurf_mod": (
            "Помогите Джейку, Трикки и Фрешу сбежать от сварливого инспектора и его собаки!\n\nМЧИСЬ так быстро, как только можешь!\n\nУВОРАЧИВАЙТЕСЬ от встречных поездов!\n\n"
            "💰 Возможности мода: Бесконечные деньги, ключи, ховерборды и бустеры\nБесплатные покупки за реальные деньги (после появления ошибки закройте окно с оплатой);\n\nВы можете прыгать бесконечное количество раз."
        ),
        "traffic_rider_org": (
            "🏍️Еще один шедевр от создателей Traffic Racer. На этот раз вы находитесь за рулем мотоцикла в гораздо более детализированном игровом процессе, но при этом сохраняете веселье и простоту старой школы.\n\n😶‍🌫️Оригинал игры."
        ),
        "traffic_rider_mod": (
            "🏍️Еще один шедевр от создателей Traffic Racer. На этот раз вы находитесь за рулем мотоцикла в гораздо более детализированном игровом процессе, но при этом сохраняете веселье и простоту старой школы.\n\n😶‍🌫️Моды: [много денег]"
        ),
        "fnaf": (
            "🐻Присматривай за аниматрониками, и ты продержишься всю ночь... возможно.\n\nПРИМЕЧАНИЕ: Ремастированная версия с версии для ПК. Для правильной работы этой игры требуется устройство с объемом оперативной памяти не менее 2 ГБ."
        ),
        "fnaf_2": (
            "🐻Некуда бежать, и ровно одно место, где можно спрятаться.\n\nПРИМЕЧАНИЕ. Обновленная версия версии для ПК. Для правильной работы этой игры требуется устройство с оперативной памятью не менее 2 ГБ."
        ),
        "clash_cl": (
            "Эпическая боевая стратегическая игра. Постройте свою деревню, тренируйте свои войска и отправляйтесь в бой!\n\nПрисоединяйтесь к миллионам игроков по всему миру, стройте свою деревню, создавайте клан и участвуйте в эпических клановых войнах!\n\nУсатые варвары, волшебники, владеющие огнем, и другие уникальные войска ждут вас! Войдите в мир Clash!"
        ),
        "clash_r": (
            "Clash Royale - это игра о сражениях лицом к лицу в реальном времени, действие которой разворачивается во вселенной Clash.\n\nВыходите на арену! Создайте свою боевую колоду и перехитрите врага в быстрых сражениях в реальном времени. От создателей CLASH OF CLANS появилась многопользовательская боевая игра в реальном времени с участием ваших любимых персонажей Clash и не только. Начните сражаться с игроками со всего мира!"
        ),
        "chess_cl": (
            "Получайте удовольствие, играя в настольную шахматную игру для двух игроков и многопользовательскую игру-головоломку!"
        ),
        "stick_war": (
            "Изучите способ владения мечом, копьем, лучником и магом. Только ты можешь спасти Инаморту!\n\nОдна из самых популярных и высокорейтинговых веб-игр всех времен теперь доступна на мобильных устройствах!"
        ),
        "snake_io": (
            "Скользить в битве. Сыграйте в эту увлекательную онлайн и оффлайн аркадную игру snake blast\n\nПройдите через новую конкурентоспособную версию Snake 🐍 и выживайте так долго, как сможете! Бросьте вызов своим друзьям и попробуйте стать самым большим червем в Snake.io!"
        ),
        "durak_online": (
            "Дурак онлайн — российская карточная игра.\n\nДурак онлайн - любимая карточная игра.\nЦель игры состоит в том, чтобы избавиться от всех своих карт. В конце игры последний игрок с картами в руке называется дураком (дурак - Дурак)."
        ),
        "granny": (
            "Бабушка держит тебя взаперти в своем доме.\n\nДобро пожаловать к бабушке.\nБабушка держит тебя взаперти в своем доме.\nТеперь вы должны попытаться выбраться из ее дома, но будьте осторожны и тихи. Она все слышит.\nЕсли ты уронишь что-нибудь на пол, она услышит это и прибежит.\nВы можете спрятаться в шкафах или под кроватями.\nУ вас есть 5 дней. Желаю удачи)"
        ),
        "bhop_pro": (
            "Возможно, вам придется много работать, но вы также можете быть профессионалом bhop.\n\nВы можете прыгать и прыгать в режиме fps с bhop pro. Вы можете доказать, что вы действительно мастер бхопа, с помощью очков и продолжительности, которые вы получите. Вы должны непрерывно поворачиваться вправо или влево и одновременно синхронно прыгать, чтобы иметь возможность делать успешные кроличьи прыжки. Bhop Pro — это портативная мобильная игра с прыжками в стиле bhop. Вы можете получить новые рейтинги, выполняя паркур-квесты. Если вы действительно можете это сделать, вы станете «профессионалом bhop»."
        ),
        "bhop_pro_mod": (
            "Возможно, вам придется много работать, но вы также можете быть профессионалом bhop.\n\nВы можете прыгать и прыгать в режиме fps с bhop pro. Вы можете доказать, что вы действительно мастер бхопа, с помощью очков и продолжительности, которые вы получите. Вы должны непрерывно поворачиваться вправо или влево и одновременно синхронно прыгать, чтобы иметь возможность делать успешные кроличьи прыжки. Bhop Pro — это портативная мобильная игра с прыжками в стиле bhop. Вы можете получить новые рейтинги, выполняя паркур-квесты. Если вы действительно можете это сделать, вы станете «профессионалом bhop».\n\n[Много денег] - Затяжные прыжки в стиле Counter Strike GO"
        ),
        "rider": (
            "Приготовьтесь к головокружительному действию!\n\nПриготовьтесь к головокружительному действию!\n\nВыполняйте безумные трюки, путешествуя по бесконечному миру Rider! Хватайте свой мотоцикл и начинайте кувыркаться, как маньяк!"
        ),
        "support_chat_btn": "✨ Чат поддержки",
        "more_modules_btn": "🔥 Другие модули",
        "strategy": "<i><b>🫡Стратегические игры</b></i>",
        "multiplayer": "<i><b>🕳️ Здесь вы найдете онлайн игры</b></i>",
        "horror": "<i><b>😁Здесь вы найдете хоррор игры</b></i>",
        "racing": "<i><b>🪄Здесь вы найдете Гоночные игры.</b></i>",
        "arcade": "<i><b>🤭Здесь вы найдете аркадные игры</b></i>",
        "back": "↙️ Назад",
        "close": "🔻 Закрыть",
    }

    @loader.command(ru_doc=".gameslist > открывает доступ к игровым категориям (можно скачивать игры прямо тут)")
    async def gameslistcmd(self, message: Message):
        """> .gameslist opens access to game categories (you can download games right here)"""
        self.chat_id = message.chat_id
        await self.inline.form(
            self.strings("categories_list"),
            reply_markup=[
                [
                    {"text": "Strategy", "callback": self.strategy},
                    {"text": "Online", "callback": self.games_multi},
                    {"text": "Horror game", "callback": self.horor_games},
                ],
                [
                    {"text": "Racing", "callback": self.racing},
                    {"text": "Arcade", "callback": self.arcade},
                ],
                [
                    {
                        "text": self.strings("more_modules_btn"),
                        "url": "https://t.me/shitmodules",
                    },
                    {
                        "text": self.strings("support_chat_btn"),
                        "url": "https://t.me/+nOXHolsAWdozODUy",
                    },
                ],
                [{"text": self.strings("close"), "action": "close"}],
            ],
            message=message,
        )

    async def strategy(self, call: InlineCall):
        await call.edit(
            text=self.strings("strategy"),
            reply_markup=[
                [
                    {"text": "Clash of Clans", "callback": self.clash_cl},
                    {"text": "Clash Royale", "callback": self.clash_r},
                ],
                [
                    {"text": "Stick War", "callback": self.stick_war},
                ],
                [
                    {"text": self.strings("back"), "callback": self._back},
                    {"text": self.strings("close"), "action": "close"},
                ],
            ],
        )

    async def games_multi(self, call: InlineCall):
        await call.edit(
            text=self.strings("multiplayer"),
            reply_markup=[
                [
                    {"text": "Snake.io", "callback": self.snake_io},
                    {"text": "Durak Online", "callback": self.durak_online},
                ],
                [
                    {"text": "bhop pro", "callback": self.bhop_pro},
                    {"text": "bhop pro mod", "callback": self.bhop_pro_mod},
                ],
                [
                    {"text": "Chess Clash", "callback": self.chess_cl},
                ],
                [
                    {"text": self.strings("back"), "callback": self._back},
                    {"text": self.strings("close"), "action": "close"},
                ],
            ],
        )

    async def horor_games(self, call: InlineCall):
        await call.edit(
            text=self.strings("horror"),
            reply_markup=[
                [
                    {"text": "FNAF", "callback": self.fnaf},
                    {"text": "FNAF2", "callback": self.fnaf_2},
                ],
                [
                    {"text": "Granny", "callback": self.granny},
                    {"text": "Antarctida", "callback": self.antarc},
                ],
                [
                    {"text": self.strings("back"), "callback": self._back},
                    {"text": self.strings("close"), "action": "close"},
                ],
            ],
        )

    async def racing(self, call: InlineCall):
        await call.edit(
            text=self.strings("racing"),
            reply_markup=[
                [
                    {"text": "Traffic Rider", "callback": self.traffic_rider_org},
                    {"text": "Traffic Rider Mod", "callback": self.traffic_rider_mod},
                ],
                [
                    {"text": "Rider", "callback": self.rider},
                    {"text": "Rally-fury", "callback": self.rally_fury},
                ],
                [
                    {"text": self.strings("back"), "callback": self._back},
                    {"text": self.strings("close"), "action": "close"},
                ],
            ],
        )

    async def arcade(self, call: InlineCall):
        await call.edit(
            text=self.strings("arcade"),
            reply_markup=[
                [
                    {"text": "SubwaySurfers Mod", "callback": self.subwaysurf_mod},
                    {"text": "SubwaySurfers", "callback": self.subwaysurf},
                ],
                [
                    {"text": "Rider", "callback": self.rider},
                ],
                [
                    {"text": self.strings("back"), "callback": self._back},
                    {"text": self.strings("close"), "action": "close"},
                ],
            ],
        )

    async def _back(self, call: InlineCall):
        await call.edit(
            self.strings("categories_list"),
            reply_markup=[
                [
                    {"text": "Strategy", "callback": self.strategy},
                    {"text": "Online", "callback": self.games_multi},
                    {"text": "Horror game", "callback": self.horor_games},
                ],
                [
                    {"text": "Racing", "callback": self.racing},
                    {"text": "Arcade", "callback": self.arcade},
                ],
                [
                    {
                        "text": self.strings("more_modules_btn"),
                        "url": "https://t.me/shitmodules",
                    },
                    {
                        "text": self.strings("support_chat_btn"),
                        "url": "https://t.me/+nOXHolsAWdozODUy",
                    },
                ],
                [{"text": self.strings("close"), "action": "close"}],
            ],
        )

    async def antarc(self, *_):
        await self.client.send_massage(
            self.chat_id, file="https://t.me/androeed_games/45188",
        )

    async def rally_fury(self, *_):
        await self.client.send_massage(
            self.chat_id, file="https://t.me/androeed_games/46160",
        )

    async def durak_online(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("durak_online"), file="https://t.me/logimeh/9",
        )

    async def snake_io(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("snake_io"), file="https://t.me/logimeh/8",
        )

    async def bhop_pro(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("bhop_pro"), file="https://t.me/logimeh/19",
        )

    async def bhop_pro_mod(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("bhop_pro_mod"), file="https://t.me/logimeh/25",
        )

    async def chess_cl(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("chess_cl"), file="https://t.me/logimeh/13",
        )

    async def clash_r(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("clash_r"), file="https://t.me/logimeh/15",
        )

    async def clash_cl(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("clash_cl"), file="https://t.me/logimeh/16",
        )

    async def stick_war(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("stick_war"), file="https://t.me/logimeh/5",
        )

    async def fnaf(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("fnaf"), file="https://t.me/logimeh/3",
        )

    async def fnaf_2(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("fnaf_2"), file="https://t.me/logimeh/4",
        )

    async def granny(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("granny"), file="https://t.me/logimeh/10",
        )

    async def traffic_rider_mod(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("traffic_rider_mod"), file="https://t.me/androeed_games/44238",
        )

    async def traffic_rider_org(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("traffic_rider_org"), file="https://t.me/androeed_games/44239",
        )

    async def rider(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("rider"), file="https://t.me/androeed_games/44239",
        )

    async def subwaysurf_mod(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("subwaysurf_mod"), file="https://t.me/logimeh/27",
        )

    async def subwaysurf(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("subway"), file="https://t.me/logimeh/26",
        )
