import sys
import copy
import threading

import utils
import consts

import imp

example = imp.load_source('example', utils.path(__file__, '../../modules/PokemonGoMap'))

class Searcher():
    def __init__(self, location, handler, step):
        self.location = location
        self.step = step

        example.process_step = utils.override(example.process_step, handler)
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
            example.FLOAT_LAT = None
            example.FLOAT_LONG = None
            return
        example.main()

    def get_args(self):
        args = copy.copy(consts.SEARCHER['ARGS']);

        args.location = self.location.toString()
        args.step_limit = self.step

        args.password = 'asdfg987'
        args.username = 'Dimitrinol'

        return args
