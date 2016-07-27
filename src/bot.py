import telepot
from telepot.delegate import per_chat_id, create_open

from libs import consts

from mixins.handlers import HandlersMixin

class Bot(HandlersMixin, telepot.helper.ChatHandler):
    @staticmethod
    def start():
        telepot.DelegatorBot(
            consts.BOT['TOKEN'],
            [(
                per_chat_id(),
                create_open(Bot, timeout = 10)
            )]
        ).message_loop(run_forever = True)
