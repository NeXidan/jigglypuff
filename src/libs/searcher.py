import sys
import copy
import time
from threading import Thread, Semaphore
from s2sphere import LatLng

import utils
import consts

pogomPath = utils.path(__file__, '../../modules/PokemonGoMap')

sys.path.append(pogomPath)

import pogom.search
import pogom.utils
from pogom import config
from pogom.models import Pokemon, create_tables

create_tables()
config['ROOT_PATH'] = pogomPath

class Searcher():
    def __init__(self, location, handler, step):
        self.location = location
        self.step = step
        self.handler = handler

    def search(self):
        args = copy.copy(pogom.utils.get_args())
        args.location = self.location.toString()
        args.step_limit = self.step

        num_steps = args.step_limit
        total_steps = (3 * (num_steps**2)) - (3 * num_steps) + 1
        position = (self.location.latitude, self.location.longitude, 0)

        if pogom.search.api._auth_provider and pogom.search.api._auth_provider._ticket_expire:
            remaining_time = pogom.search.api._auth_provider._ticket_expire/1000 - time.time()

            if remaining_time < 60:
                pogom.search.login(args, position)
        else:
            pogom.search.login(args, position)

        sem = Semaphore()

        search_threads = []
        curr_steps = 0
        max_threads = args.num_threads

        for step, step_location in enumerate(pogom.search.generate_location_steps(position, num_steps), 1):
            search_args = (0, total_steps, step_location, step, sem)
            search_threads.append(Thread(target=pogom.search.search_thread, name='search_step_thread {}'.format(step), args=(search_args, )))

            if step % max_threads == 0:
                curr_steps = self.process_search_threads(search_threads, curr_steps, total_steps)
                search_threads = []

        if search_threads:
            self.process_search_threads(search_threads, curr_steps, total_steps)

    def process_search_threads(self, search_threads, curr_steps, total_steps):
        for thread in search_threads:
            thread.start()
        for thread in search_threads:
            curr_steps += 1
            thread.join()
            self.handler(self.getPokemons(), curr_steps, total_steps)
        return curr_steps

        # args.password = 'asdfg987'
        # args.username = 'Dimitrinol'

    def getPokemons(self):
        pokemon_list = []
        for pokemon in Pokemon.get_active():
            pokemon_point = LatLng.from_degrees(pokemon['latitude'], pokemon['longitude'])
            entry = {
                'id': pokemon['pokemon_id'],
                'name': pokemon['pokemon_name'],
                # 'time_to_disappear': '%dm %ds' % (divmod((pokemon['disappear_time']-datetime.utcnow()).seconds, 60)),
                'latitude': pokemon['latitude'],
                'longitude': pokemon['longitude']
            }
            pokemon_list.append(entry)
        # pokemon_list = [y[0] for y in sorted(pokemon_list, key=lambda x: x[1])]
        return pokemon_list
