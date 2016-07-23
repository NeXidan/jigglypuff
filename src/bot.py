import telepot

from libs import utils, consts
from map import Map

class Bot():
    bot = telepot.Bot(consts.BOT['TOKEN'])

    def __init__(self):
        self.bot.message_loop(self.message)

    def message(self, msg):
        contentType, chatType, chatId = telepot.glance(msg)

        self.chatId = chatId;

        if not hasattr(self, contentType):
            self.unknown(msg);
            return

        getattr(self, contentType)(msg)

    def unknown(self, msg):
        self.bot.sendSticker(self.chatId, consts.BOT['STICKER'])
        self.bot.sendMessage(self.chatId, 'Jigglypuff is so sorry')

    def location(self, msg):
        Map(
            location = msg['location'],
            callback = self.sendPhoto
        )

    def sendPhoto(self, image):
        path = utils.path(__file__, '../tmp/' + str(self.chatId) + '.png')
        image.save(path, 'PNG')
        with open(path, 'rb') as imageFile:
            self.bot.sendPhoto(self.chatId, imageFile)
