import telepot
from telepot.delegate import per_chat_id, create_open

from libs import utils, consts
from map import Map

COMMAND_SLASH = '/'
COMMAND_PREFIX = 'command_'

class Bot(telepot.helper.ChatHandler):
    @staticmethod
    def start():
        telepot.DelegatorBot(
            consts.BOT['TOKEN'],
            [(per_chat_id(), create_open(Bot, timeout = 10))]
        ).message_loop(run_forever = True)

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
                path = utils.path(__file__, '../tmp/' + str(self.chat_id) + '.png')
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

    def command_stop(self, msg):
        self.sender.sendMessage('You cannot stop *Jigglypuff*', parse_mode = 'Markdown')

    def command_keyboard(self, msg):
        if not hasattr(self, 'keyboard'):
            self.keyboard = telepot.message_identifier(self.sender.sendMessage(
                'Use this keyboard to interact with *Jigglypuff*',
                parse_mode = 'Markdown',
                reply_markup = consts.BOT['KEYBOARD']['SHOW']
            ))
            return

        self.sender.sendMessage(
            '*Jigglypuff* will hide keyboard',
            parse_mode = 'Markdown',
            reply_markup = consts.BOT['KEYBOARD']['HIDE']
        )
        del self.keyboard

    def command_help(self, msg):
        self.sender.sendMessage(consts.HELP_MESSAGE, parse_mode = 'Markdown')
