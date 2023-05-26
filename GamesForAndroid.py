__version__ = (1, 0, 4)
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

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/GamesForAndroid.jpeg
# meta banner: https://raw.githubusercontent.com/kamolgks/assets/main/GamesForAndroid.jpg

# meta developer: @shitmodules

import logging

from .. import loader
from telethon.tl.types import Message
from ..inline.types import InlineCall

logger = logging.getLogger(__name__)


@loader.tds
class GamesForAndroid(loader.Module):
    """Hacked android games (All in categories, choose what you like and download.)"""

    strings = {
        "name": "GamesForAndroid",
        "categories_list": (
            "<b>🙂Here is a list of game categories:\n"
            "Strategy games | Online games | Horror games | "
            "Racing Games | Arcade\n\n⚠️ All games and their categories are taken from the Internet.</b>"
        ),
        "subway": (
            "Help Jake, Tricky and Fresh escape from the grumpy inspector and his dog!\n\n"
            "DRIVE as fast as you can!\n\nDOVER the oncoming trains!"
        ),
        "subwaysurf_mod": (
            "Help Jake, Tricky and Fresh escape from the grumpy Inspector and his dog!\n\nDRIVE as fast as you can!\n\n"
            "DOUD oncoming trains!\n\n💰 Mod features: Infinite money, keys, hoverboards and boosters\n"
            "Free purchases with real money (close the payment window after the error appears);\n\nYou can jump an infinite number of times."
        ),
        "traffic_rider_org": (
            "🏍Another masterpiece from the creators of Traffic Racer. This time you are behind the wheel of a motorcycle in a much more "
            "detailed gameplay, yet retaining the fun and simplicity of the old school.\n\n😶‍🌫️Original game."
        ),
        "traffic_rider_mod": (
            "🏍Another masterpiece from the creators of Traffic Racer. This time you are behind the wheel of a motorcycle in a much more "
            "detailed gameplay, yet retaining the fun and simplicity of the old school.\n\n😶‍🌫️Mods: [a lot of money]"
        ),
        "fnaf": (
            "🐻Keep an eye on the animatronics and you'll last all night...maybe.\n\nNOTE: Remastered version"
            "From the PC version. This game requires a device with at least 2 GB of RAM to run properly."
        ),
        "fnaf_2": (
            "🐻Nowhere to run, and exactly one place to hide.\n\nNOTE: An updated version of the PC version."
            "This game requires a device with at least 2 GB of RAM to run properly."
        ),
        "clash_cl": (
            "An epic combat strategy game. Build your village, train your troops and go to battle!\n\n"
            "Join millions of players around the world, build your village, create a clan and participate in epic clan wars!\n\n"
            "Mustache barbarians, fire-wielding wizards and other unique troops await! Enter the world of Clash!"
        ),
        "clash_r": (
            "Clash Royale is a real-time face-to-face combat game set in the Clash universe.\n\n"
            "Enter the arena! Build your battle deck and outsmart the enemy in fast-paced real-time battles. From the makers of CLASH OF CLANS"
            "A real-time multiplayer combat game featuring your favorite Clash characters and more is here. Start fighting against players from all over the world!"
        ),
        "chess_cl": (
            "Have fun playing two player board chess game and multiplayer puzzle game!"
        ),
        "stick_war": (
            "Learn how to wield a sword, spear, archer, and mage. Only you can save Inamorta!\n\n"
            "One of the most popular and highest rated web games of all time is now available on mobile!"
        ),
        "snake_io": (
            "Slither into battle. Play this fun online and offline snake blast arcade game\n\n"
            "Go through the new competitive version of Snake 🐍 and survive for as long as you can!"
            "Challenge your friends and try to be the biggest worm in Snake.io!"
        ),
        "durak_online": (
            "Durak online is a Russian card game.\n\nDurak online is my favorite card game.\n"
            "The goal of the game is to get rid of all your cards. At the end of the game, the last player with cards in hand is called the fool"
            "(Fool - Fool)."
        ),
        "granny": (
            "Grandma keeps you locked up in her house.\n\nWelcome to grandma.\n"
            "Grandma keeps you locked up in her house.\nNow you should try to get out of her house, but be careful and quiet."
            "She hears everything.\nIf you drop something on the floor, she will hear it and come running.\nYou can hide in closets or under beds.\n"
            "You have 5 days. Good luck)"
        ),
        "bhop_pro": (
            "You may have to work hard, but you can also be a bhop pro.\n\n"
            "You can jump and jump in fps mode with bhop pro. You can prove that you are truly a bhop master,"
            "with the help of the points and duration you get. You have to continuously turn right or left and "
            "Jump in sync at the same time to be able to make successful bunny jumps. Bhop Pro is portable"
            "a bhop style jumping mobile game. You can get new rankings by doing parkour quests. If you really "
            "if you can do that, you'll be a 'bhop pro'."
        ),
        "bhop_pro_mod": (
            "You may have to work hard, but you can also be a bhop pro.\n\n"
            "You can jump and jump in fps mode with bhop pro. You can prove that you are truly a bhop master with glasses and "
            "the duration you get. You must continuously turn to the right or left and jump in sync at the same time, "
            "to be able to make successful bunny jumps. Bhop Pro is a portable mobile bhop jumping game."
            "You can get new ratings by completing parkour quests. If you can really do it, you will become a 'bhop pro'.\n\n"
            "[Lots of money] - Counter Strike GO style high jumps"
        ),
        "rider": (
            "Get ready for some mind-blowing action!\n\nGet ready for some mind-blowing action!\n\n"
            "Perform insane stunts as you travel through the endless world of Rider! Grab your bike and start tumbling like a maniac!"
        ),
        "brawl": (
            "Brawl Stars - The long-awaited action game from Supercell"
        ),
        "brawl_vzlom": (
            "Brawl Stars [Unlimited Money] - The long-awaited action game from Supercell\n------------\n💰 Mod features: Null&rsquo;s "
            "Brawl&nbsp;private server with a lot of money, tickets and gems (installed separately from the original version of the game)."
            "The private server does not contain content that is added with the latest updates of the original."
        ),
        "bowmaster": (
            "Bowmasters - Arcade shooter with bows and physics"
        ),
        "bowmaster_vzlom": (
            "Bowmasters [Unlimited Money] - Arcade shooter with bows and physics\n------------\n💰 Mod features: "
            "Endless coins and stones; All characters are open."
        ),
        "driving": (
            "Driving Zone: Germany - Realistic car simulator with German cars"
        ),
        "driving_vzlom": (
            "Driving Zone: Germany [Unlocked] - Realistic car simulator with German cars\n------------\n"
            "💰 Mod features: Unlocked all cars."
        ),
        "antarc": (
            "Antarctica 88: Horror Action Survival Game - Original action horror game with multiple endings"
        ),
        "rally_fury": (
            "Rally Fury - Extreme Racing - High-speed race with realistic physics"
        ),
        "among_us": (
            "Among Us - Unique arcade action game with multiplayer"
        ),
        "among_us_mod": (
            "Among Us [Unlocked] - Unique arcade action game with multiplayer\n------------\n"
            "💰 Mod features: All clothes and pets are unlocked (after opening the wardrobe, you need to wait a "
            "while before all the clothes textures are loaded). \nAuthorization through Google does not work!"
        ),
        "support_chat_btn": "✨ Support Chat",
        "more_modules_btn": "🔥 More Modules",
        "strategy": "<b>🫡Strategy games</b>",
        "multiplayer": "<b>🕳️Here you will find multiplayer games</b>",
        "horror": "<b>😁Here you will find arcade games</b>",
        "racing": "<b>🪄Here you will find Racing games</b>",
        "arcade": "<b>🤭Here you will find arcade games</b>",
        "back": "↙️ Back",
        "close": "🔻 Close",
    }

    strings_ru = {
        "categories_list": (
            "<b>🙂Вот список категорий игр:\n"
            "Стратегические игры | Онлайн игры | Хоррор игры | "
            "Гоночные игры | Аркады\n\n⚠️ Все игры и их категории взяты из Интернета.</b>"
        ),
        "subway": (
            "Помогите Джейку, Трикки и Фрешу сбежать от сварливого инспектора и его собаки!\n\n"
            "МЧИСЬ так быстро, как только можешь!\n\nУВОРАЧИВАЙТЕСЬ от встречных поездов!"
        ),
        "subwaysurf_mod": (
            "Помогите Джейку, Трикки и Фрешу сбежать от сварливого инспектора и его собаки!\n\nМЧИСЬ так быстро, как только можешь!\n\n"
            "УВОРАЧИВАЙТЕСЬ от встречных поездов!\n\n💰 Возможности мода: Бесконечные деньги, ключи, ховерборды и бустеры\n"
            "Бесплатные покупки за реальные деньги (после появления ошибки закройте окно с оплатой);\n\nВы можете прыгать бесконечное количество раз."
        ),
        "traffic_rider_org": (
            "🏍️Еще один шедевр от создателей Traffic Racer. На этот раз вы находитесь за рулем мотоцикла в гораздо более "
            "детализированном игровом процессе, но при этом сохраняете веселье и простоту старой школы.\n\n😶‍🌫️Оригинал игры."
        ),
        "traffic_rider_mod": (
            "🏍️Еще один шедевр от создателей Traffic Racer. На этот раз вы находитесь за рулем мотоцикла в гораздо более "
            "детализированном игровом процессе, но при этом сохраняете веселье и простоту старой школы.\n\n😶‍🌫️Моды: [много денег]"
        ),
        "fnaf": (
            "🐻Присматривай за аниматрониками, и ты продержишься всю ночь... возможно.\n\nПРИМЕЧАНИЕ: Ремастированная версия "
            "с версии для ПК. Для правильной работы этой игры требуется устройство с объемом оперативной памяти не менее 2 ГБ."
        ),
        "fnaf_2": (
            "🐻Некуда бежать, и ровно одно место, где можно спрятаться.\n\nПРИМЕЧАНИЕ. Обновленная версия версии для ПК. "
            "Для правильной работы этой игры требуется устройство с оперативной памятью не менее 2 ГБ."
        ),
        "clash_cl": (
            "Эпическая боевая стратегическая игра. Постройте свою деревню, тренируйте свои войска и отправляйтесь в бой!\n\n"
            "Присоединяйтесь к миллионам игроков по всему миру, стройте свою деревню, создавайте клан и участвуйте в эпических клановых войнах!\n\n"
            "Усатые варвары, волшебники, владеющие огнем, и другие уникальные войска ждут вас! Войдите в мир Clash!"
        ),
        "clash_r": (
            "Clash Royale - это игра о сражениях лицом к лицу в реальном времени, действие которой разворачивается во вселенной Clash.\n\n"
            "Выходите на арену! Создайте свою боевую колоду и перехитрите врага в быстрых сражениях в реальном времени. От создателей CLASH OF CLANS "
            "появилась многопользовательская боевая игра в реальном времени с участием ваших любимых персонажей Clash и не только. Начните сражаться с игроками со всего мира!"
        ),
        "chess_cl": (
            "Получайте удовольствие, играя в настольную шахматную игру для двух игроков и многопользовательскую игру-головоломку!"
        ),
        "stick_war": (
            "Изучите способ владения мечом, копьем, лучником и магом. Только ты можешь спасти Инаморту!\n\n"
            "Одна из самых популярных и высокорейтинговых веб-игр всех времен теперь доступна на мобильных устройствах!"
        ),
        "snake_io": (
            "Скользить в битве. Сыграйте в эту увлекательную онлайн и оффлайн аркадную игру snake blast\n\n"
            "Пройдите через новую конкурентоспособную версию Snake 🐍 и выживайте так долго, как сможете! "
            "Бросьте вызов своим друзьям и попробуйте стать самым большим червем в Snake.io!"
        ),
        "durak_online": (
            "Дурак онлайн — российская карточная игра.\n\nДурак онлайн - любимая карточная игра.\n"
            "Цель игры состоит в том, чтобы избавиться от всех своих карт. В конце игры последний игрок с картами в руке называется дураком "
            "(дурак - Дурак)."
        ),
        "granny": (
            "Бабушка держит тебя взаперти в своем доме.\n\nДобро пожаловать к бабушке.\n"
            "Бабушка держит тебя взаперти в своем доме.\nТеперь вы должны попытаться выбраться из ее дома, но будьте осторожны и тихи. "
            "Она все слышит.\nЕсли ты уронишь что-нибудь на пол, она услышит это и прибежит.\nВы можете спрятаться в шкафах или под кроватями.\n"
            "У вас есть 5 дней. Желаю удачи)"
        ),
        "bhop_pro": (
            "Возможно, вам придется много работать, но вы также можете быть профессионалом bhop.\n\n"
            "Вы можете прыгать и прыгать в режиме fps с bhop pro. Вы можете доказать, что вы действительно мастер бхопа, "
            "с помощью очков и продолжительности, которые вы получите. Вы должны непрерывно поворачиваться вправо или влево и "
            "одновременно синхронно прыгать, чтобы иметь возможность делать успешные кроличьи прыжки. Bhop Pro — это портативная "
            "мобильная игра с прыжками в стиле bhop. Вы можете получить новые рейтинги, выполняя паркур-квесты. Если вы действительно "
            "можете это сделать, вы станете «профессионалом bhop»."
        ),
        "bhop_pro_mod": (
            "Возможно, вам придется много работать, но вы также можете быть профессионалом bhop.\n\n"
            "Вы можете прыгать и прыгать в режиме fps с bhop pro. Вы можете доказать, что вы действительно мастер бхопа, с помощью очков и "
            "продолжительности, которые вы получите. Вы должны непрерывно поворачиваться вправо или влево и одновременно синхронно прыгать, "
            "чтобы иметь возможность делать успешные кроличьи прыжки. Bhop Pro — это портативная мобильная игра с прыжками в стиле bhop. "
            "Вы можете получить новые рейтинги, выполняя паркур-квесты. Если вы действительно можете это сделать, вы станете «профессионалом bhop».\n\n"
            "[Много денег] - Затяжные прыжки в стиле Counter Strike GO"
        ),
        "rider": (
            "Приготовьтесь к головокружительному действию!\n\nПриготовьтесь к головокружительному действию!\n\n"
            "Выполняйте безумные трюки, путешествуя по бесконечному миру Rider! Хватайте свой мотоцикл и начинайте кувыркаться, как маньяк!"
        ),
        "brawl": (
            "Brawl Stars — долгожданный экшен от Supercell."
        ),
        "brawl_vzlom": (
            "Brawl Stars [Бесконечные деньги] - Долгожданный экшн от Supercell\n-------------\n💰 Особенности мода: Null&rsquo;s"
            "Приватный сервер Brawl&nbsp;с кучей денег, билетов и самоцветов (устанавливается отдельно от оригинальной версии игры)\n"
            "Частный сервер не содержит контента, добавленного с последними обновлениями оригинала."
        ),
        "bowmaster": (
            "Bowmasters - Аркадный шутер с луками и физикой."
        ),
        "bowmaster_vzlom": (
            "Bowmasters [Бесконечные деньги] - Аркадный шутер с луками и физикой\n-------------\n💰 Особенности мода: "
            "Бесконечные монеты и камни; все символы открыты."
        ),
        "driving": (
            "Drive Zone: Germany - Реалистичный автомобильный симулятор с немецкими автомобилями"
        ),
        "driving_vzlom": (
            "Driveing Zone: Germany [Unlocked] - Реалистичный автосимулятор с немецкими автомобилями\n------------\n"
            "💰 Особенности мода: Разблокированы все машины."
        ),
        "antarc": (
            "Antarctica 88: Horror Action Survival Game — оригинальная хоррор-игра с несколькими концовками."
        ),
        "rally_fury": (
            "Rally Fury - Extreme Racing - Скоростная гонка с реалистичной физикой"
        ),
        "among_us": (
            "Among Us - Уникальный аркадный экшен с мультиплеером"
        ),
        "among_us_mod": (
            "Among Us [Unlocked] - Уникальная аркадная игра в жанре экшн с мультиплеером\n-------------\n"
            "💰 Особенности мода: Разблокирована вся одежда и питомцы (после открытия шкафа нужно подождать "
            "пока до этого все текстуры одежды подгружаются).\nАвторизация через гугл не работает!"
        ),
        "support_chat_btn": "✨ Чат поддержки",
        "more_modules_btn": "🔥 Другие модули",
        "strategy": "<b>🫡Стратегические игры</b>",
        "multiplayer": "<b>🕳️ Здесь вы найдете онлайн игры</b>",
        "horror": "<b>😁Здесь вы найдете хоррор игры</b>",
        "racing": "<b>🪄Здесь вы найдете Гоночные игры.</b>",
        "arcade": "<b>🤭Здесь вы найдете аркадные игры</b>",
        "back": "↙️ Назад",
        "close": "🔻 Закрыть",
    }

    @loader.command(
        ru_doc=".gameslist > открывает доступ к игровым категориям (можно скачивать игры прямо тут)",
    )
    async def gameslist(self, message: Message):
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
                        "url": "http://t.me/shitmodules_chat",
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
                    {"text": "Brawl Stars", "callback": self.brawl},
                    {"text": "Stick War", "callback": self.stick_war},
                ],
                [
                    {"text": "Brawl Stars (mod money)",
                     "callback": self.brawl_vzlom},
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
                    {"text": "Among Us", "callback": self.among_us},
                ],
                [
                    {"text": "Among Us(mod)", "callback": self.among_us_mod},
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
                    {"text": "Traffic Rider Mod",
                        "callback": self.traffic_rider_mod},
                ],
                [
                    {"text": "Rider", "callback": self.rider},
                    {"text": "Rally-fury", "callback": self.rally_fury},
                ],
                [
                    {"text": "Driving Zone", "callback": self.driving},
                    {"text": "Driving Zone(mod)",
                     "callback": self.driving_vzlom},
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
                    {"text": "Bowmasters", "callback": self.bowmaster},
                ],
                [
                    {"text": "Bowmasters(mod)",
                     "callback": self.bowmaster_vzlom},
                    {"text": "Among Us", "callback": self.among_us},
                ],
                [
                    {"text": "Among Us(mod)", "callback": self.among_us_mod},
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
                        "url": "http://t.me/shitmodules_chat",
                    },
                ],
                [{"text": self.strings("close"), "action": "close"}],
            ],
        )

    async def antarc(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("antarc"), file="https://t.me/logimeh/39",
        )

    async def rally_fury(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("rally_fury"), file="https://t.me/logimeh/38",
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
            self.chat_id, self.strings("traffic_rider_mod"), file="https://t.me/logimeh/40",
        )

    async def traffic_rider_org(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("traffic_rider_org"), file="https://t.me/logimeh/42",
        )

    async def rider(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("rider"), file="https://t.me/logimeh/44",
        )

    async def subwaysurf_mod(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("subwaysurf_mod"), file="https://t.me/logimeh/46",
        )

    async def subwaysurf(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("subway"), file="https://t.me/logimeh/52",
        )

    async def brawl(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("brawl"), file="https://t.me/logimeh/58",
        )

    async def brawl_vzlom(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("brawl_vzlom"), file="https://t.me/logimeh/54",
        )

    async def bowmaster(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("bowmaster"), file="https://t.me/logimeh/51",
        )

    async def bowmaster_vzlom(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("bowmaster_vzlom"), file="https://t.me/logimeh/50",
        )

    async def driving(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("driving"), file="https://t.me/logimeh/48",
        )

    async def driving_vzlom(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("driving_vzlom"), file="https://t.me/logimeh/47",
        )

    async def among_us(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("among_us"), file="https://t.me/logimeh/61",
        )

    async def among_us_mod(self, *_):
        await self.client.send_message(
            self.chat_id, self.strings("among_us_mod"), file="https://t.me/logimeh/59",
        )
