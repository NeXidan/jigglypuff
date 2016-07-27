import telepot

from commands import CommandsMixin

from ..libs import utils, consts
from ..map import Map

COMMAND_SLASH = '/'
COMMAND_PREFIX = 'command_'

class HandlersMixin(CommandsMixin):
    def on_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        if hasattr(self, content_type):
            return getattr(self, content_type)(msg)

        self.unknown(msg);

    def unknown(self, msg):
        self.sender.sendSticker(consts.BOT['STICKER'])
        self.sender.sendMessage('Jigglypuff is so sorry')

    def location(self, msg, step = 5):
        reply = telepot.message_identifier(self.sender.sendMessage(consts.BOT['LOCATION']['REPLY'] % (0, 0), parse_mode = 'Markdown'))

        def handler(pokemons = None, image = None, current_steps = 0, total_steps = 0):
            self.bot.editMessageText(reply, consts.BOT['LOCATION']['REPLY'] % (current_steps, total_steps), parse_mode = 'Markdown')
            if image is not None:
                path = utils.path(__file__, '../../tmp/' + str(self.chat_id) + '.png')
                image.save(path, 'PNG')
                with open(path, 'rb') as imageFile:
                    self.sender.sendPhoto(imageFile)

        Map(location = msg['location'], callback = handler, step = step)

    def text(self, msg):
        content = msg['text']

        if content[0] == '/':
            command = COMMAND_PREFIX + content[1:]

            if hasattr(self, command):
                return getattr(self, command)(msg)

        self.unknown(msg)
