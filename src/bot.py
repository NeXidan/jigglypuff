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

    def location(self, msg, step = 4):
        maxStep = step ** 2
        reply = (
            self.chatId,
            self.bot.sendMessage(self.chatId, consts.BOT['LOCATION']['REPLY'] % (0, maxStep), parse_mode = 'Markdown')['message_id']
        )

        def handler(pokemons, image = None, current = 0):
            self.bot.editMessageText(reply, consts.BOT['LOCATION']['REPLY'] % (current, maxStep), parse_mode = 'Markdown')
            if image is not None:
                path = utils.path(__file__, '../tmp/' + str(self.chatId) + '.png')
                image.save(path, 'PNG')
                with open(path, 'rb') as imageFile:
                    self.bot.sendPhoto(self.chatId, imageFile)



        Map(
            location = msg['location'],
            callback = handler,
            step = step
        )
