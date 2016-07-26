import sys
import copy
import time
from threading import Thread, Semaphore
from s2sphere import LatLng
from datetime import datetime

import utils
import consts

sys.path.append(utils.path(__file__, '../../modules/PokemonGoMap'))

import pogom.search
import pogom.utils
from pogom.models import Pokemon

class Searcher():
    def __init__(self, location, handler, step):
        self.location = location
        self.step = step
        self.handler = handler

    def search(self):
        args = copy.copy(pogom.utils.get_args())
        args.location = self.location.to_string()
        args.step_limit = self.step

        num_steps = args.step_limit
        total_steps = (3 * (num_steps**2)) - (3 * num_steps) + 1
        position = (self.location.latitude, self.location.longitude, 0)

        if pogom.search.api._auth_provider and pogom.search.api._auth_provider._ticket_expire:
            remaining_time = pogom.search.api._auth_provider._ticket_expire / 1000 - time.time()

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
            search_thread = Thread(
                target = pogom.search.search_thread,
                name = 'search_step_thread {}'.format(step),
                args = (search_args, )
            )
            search_thread.start()
            search_threads.append(search_thread)

            while len(search_threads) == max_threads:
                for index, thread in enumerate(search_threads):
                    if not thread.is_alive():
                        del search_threads[index]
                        curr_steps += 1
                        self.handler(None, curr_steps, total_steps)

        for thread in search_threads:
            curr_steps += 1
            thread.join()
            self.handler(self.get_pokemons() if curr_steps == total_steps else None, curr_steps, total_steps)

    def get_pokemons(self):
        pokemon_list = []
        origin_point = LatLng.from_degrees(self.location.latitude, self.location.longitude)
        for pokemon in Pokemon.get_active():
            pokemon_point = LatLng.from_degrees(pokemon['latitude'], pokemon['longitude'])

            pokemon_list.append({
                'id': pokemon['pokemon_id'],
                'name': pokemon['pokemon_name'],
                'time': '%02d:%02d' % (divmod((pokemon['disappear_time'] - datetime.utcnow()).seconds, 60)),
                'latitude': pokemon['latitude'],
                'longitude': pokemon['longitude']
            })

        return pokemon_list
