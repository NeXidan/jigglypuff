import telepot

from ..libs import consts

class CommandsMixin():
    def command_stop(self, msg):
        self.sender.sendMessage('You cannot stop *Jigglypuff*', parse_mode = 'Markdown')

    def command_help(self, msg):
        self.sender.sendMessage(consts.BOT['HELP'], parse_mode = 'Markdown')

    def command_ping(self, msg):
        self.sender.sendMessage('Pong!');

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
