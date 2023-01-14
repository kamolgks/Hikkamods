__version__ = (0, 0, 1)
#   ___    _         _                             _         _                
#  (  _`\ ( )     _ ( )_                          ( )       (_ )              
#  | (_(_)| |__  (_)| ,_)     ___ ___     _      _| | _   _  | |    __    ___ 
#  `\__ \ |  _ `\| || |     /' _ ` _ `\ /'_`\  /'_` |( ) ( ) | |  /'__`\/',__)
#  ( )_) || | | || || |_    | ( ) ( ) |( (_) )( (_| || (_) | | | (  ___/\__, \
#  `\____)(_) (_)(_)`\__)   (_) (_) (_)`\___/'`\__,_)`\___/'(___)`\____)(____/
#        
#            © Copyright 2022
#
#          https://t.me/shitmodules
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: hikka_only 
# scope: hikka_min 1.6.0

# meta developer: @shitmodules

from .. import loader, utils
from telethon.tl.types import Message
import random

photos = [
    {"photo": "https://ibb.co/GVcfq7K"},
    {"photo": "https://ibb.co/DQgnfL3"},
    {"photo": "https://ibb.co/FhHsffW"},
    {"photo": "https://ibb.co/NTyw41q"},
    {"photo": "https://ibb.co/gJTQtTf"},
    {"photo": "https://ibb.co/2F5XwtT"},
    {"photo": "https://ibb.co/GHLqjxt"},
    {"photo": "https://ibb.co/frMxckH"},
    {"photo": "https://ibb.co/QD9Pghr"},
    {"photo": "https://ibb.co/GHLqjxt"},
    {"photo": "https://ibb.co/c3T75J3"},
    {"photo": "https://ibb.co/dgMGpj6"},
    {"photo": "https://ibb.co/0G9sQg2"},
    {"photo": "https://ibb.co/FVKJQGp"},
    {"photo": "https://i.imgur.com/5ugBW8K.jpeg"},
    {"photo": "https://i.imgur.com/QJoFN4y.jpeg"},
    {"photo": "https://imgur.io/Z4uZZHx?r"},
]

def generate_caption() -> str:
  return random.choice(["Your gallery is ready🙃", "Thanks for using, keep your inline gallery!😁"])


async def random_photo() -> str:
    sex = random.choice(photos)
    return sex["photo"]

@loader.tds
class GachiGalleryMod(loader.Module):
  """random gachimuchi photos and memes"""
  
  strings = {"name": "GachiGallery"}
  
  @loader.command(ru_doc="Скидывает инлайн галерею с мемами (гачи мемы)")
  async def gachicmd(self, message: Message):
    """.gachi > sends random gachi photos and memes"""
    await self.inline.gallery(message, random_photo, caption=generate_caption,)
