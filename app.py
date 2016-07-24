import sys

from src.bot import Bot

from src.libs import utils
path = utils.path(__file__, 'modules/PokemonGoMap')
sys.path.append(path)

import pogom

pogom.models.create_tables()
pogom.config['ROOT_PATH'] = path

def main():
    try:
        Bot.start()
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()
