import sys
import copy
import threading

import utils
import consts

sys.path.append(utils.path(__file__, '../../modules/PokemonGoMap'))
import example

class Searcher():
    def __init__(self, location, callback):
        self.location = location

        example.process_step = utils.override(example.process_step, callback)
        example.get_args = self.get_args
        example.register_background_thread = self.register_background_thread

    def call(self, method, **kwargs):
        if not hasattr(self, method):
            return getattr(example, method)(**kwargs)

        return getattr(self, method)(**kwargs)

    def get(self, property):
        if not hasattr(self, property):
            return getattr(example, property)

        return getattr(self, property)

    def register_background_thread(self, initial_registration=False):
        if not initial_registration:
            return

        example.search_thread = threading.Thread(target = example.main)

        example.search_thread.daemon = True
        example.search_thread.name = 'search_thread'
        example.search_thread.start()

    def get_args(self):
        args = copy.copy(consts.SEARCHER['ARGS']);

        args.location = self.location.toString()

        args.password = 'asdfg987'
        args.step_limit = '3'
        args.username = 'Dimitrinol'

        return args
