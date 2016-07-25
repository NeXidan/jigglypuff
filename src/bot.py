import telepot
from telepot.delegate import per_chat_id, create_open

from libs import utils, consts
from map import Map

class Bot(telepot.helper.ChatHandler):
    @staticmethod
    def start():
        telepot.DelegatorBot(
            consts.BOT['TOKEN'],
            [(per_chat_id(), create_open(Bot, timeout = 10))]
        ).message_loop(run_forever = True)

    def on_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        if not hasattr(self, content_type):
            self.unknown(msg);
            return

        getattr(self, content_type)(msg)

    def unknown(self, msg):
        self.sender.sendSticker(consts.BOT['STICKER'])
        self.sender.sendMessage('Jigglypuff is so sorry')

    def location(self, msg, step = 5):
        reply = telepot.message_identifier(self.sender.sendMessage(consts.BOT['LOCATION']['REPLY'] % (0, 0), parse_mode = 'Markdown'))

        def handler(pokemons, image = None, current_steps = 0, total_steps = 0):
            self.bot.editMessageText(reply, consts.BOT['LOCATION']['REPLY'] % (current_steps, total_steps), parse_mode = 'Markdown')
            if image is not None:
                path = utils.path(__file__, '../tmp/' + str(self.chat_id) + '.png')
                image.save(path, 'PNG')
                with open(path, 'rb') as imageFile:
                    self.sender.sendPhoto(imageFile)

        Map(location = msg['location'], callback = handler, step = step)
