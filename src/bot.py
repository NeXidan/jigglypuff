import telepot

from libs import utils
from map import Map
import consts

class Bot():
    bot = telepot.Bot(consts.BOT['TOKEN'])

    def __init__(self):
        self.bot.message_loop(self.message)

    def message(self, msg):
        contentType, chatType, chatId = telepot.glance(msg)

        if not hasattr(self, contentType):
            self.unknown(msg);
            return

        getattr(self, contentType)(msg)

    def unknown(self, msg):
        chatId = msg['chat']['id']

        self.bot.sendSticker(chatId, consts.BOT['STICKER'])
        self.bot.sendMessage(chatId, 'Jigglypuff is so sorry')

    def location(self, msg):
        self.map = Map(msg['location'])
        path = utils.path('tmp/' + str(msg['chat']['id']) + '.png')

        self.map.image.save(path, 'PNG')

        with open(path, 'rb') as image:
            self.bot.sendPhoto(msg['chat']['id'], image, utils.locationToString(self.map.location))
