import requests
from io import BytesIO
from PIL import Image, ImageDraw

from libs import utils, consts
from libs.searcher import Searcher

from libs.geom.location import Location

class Map():
    def __init__(self, location, callback, step):
        self.location = Location.factory(location)
        self.step = step
        self.callback = callback

        location_string = self.location.to_string()

        data = {
            'zoom': consts.MAP['ZOOM'],
            'center': location_string,
            'markers': location_string
        }

        data.update(consts.MAP['API']['PARAMS'])

        response = requests.get(consts.MAP['API']['URL'], data, stream=True)
        response.raw.decode_content = True
        self.image = Image.open(BytesIO(response.content)).convert('RGBA')

        Searcher(
            location = self.location,
            handler = self.handler,
            step = self.step
        ).search()


    def handler(self, pokemons, curr_steps, total_steps):
        image = None
        if pokemons:
            image = self.draw_image(pokemons)

        self.callback(pokemons, image, curr_steps, total_steps)

    def draw_image(self, pokemons):
        image = self.image.copy()
        for pokemon in pokemons:
            self.draw_pokemon(image, pokemon)

        return image

    def draw_pokemon(self, image, pokemon):
        pokemon_image = Image \
            .open(utils.path(__file__, '../modules/PokemonGoMap/static/icons/' + str(pokemon['id']) + '.png')) \
            .convert('RGBA')

        offset = utils.build_offset(
            point = Location.factory(pokemon),
            center = self.location,
            size = consts.SIZE,
            zoom = consts.MAP['ZOOM']
        )

        image.paste(
            pokemon_image,
            (
                offset[0] - pokemon_image.size[0] / 2,
                offset[1] - pokemon_image.size[1] / 2
            ),
            mask = pokemon_image
        )

        ImageDraw.Draw(image).text(
            (
                offset[0] - pokemon_image.size[0] / 2,
                offset[1] + pokemon_image.size[1] / 2
            ),
            pokemon['time'],
            (0, 0, 0)
        )
