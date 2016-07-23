import requests

from PIL import Image

from libs import utils, consts
from libs.searcher import Searcher

from libs.geom.location import Location

class Map():
    current = 0

    def __init__(self, location, callback, step):
        self.location = Location.fromTelegramLocation(location)
        self.step = step
        self.callback = callback

        locationString = self.location.toString()

        data = {
            'zoom': consts.MAP['ZOOM'] - self.step,
            'center': locationString,
            'markers': locationString
        }

        data.update(consts.MAP['API']['PARAMS'])

        response = requests.get(consts.MAP['API']['URL'], data, stream=True)
        response.raw.decode_content = True
        self.image = Image.open(response.raw).convert('RGBA')

        self.searcher = Searcher(
            location = self.location,
            handler = self.handler,
            step = self.step
        )

        self.searcher.call('register_background_thread', initial_registration=True)

    def handler(self):
        pokemons = self.searcher.get('pokemons')

        image = None
        self.current += 1
        if self.current == self.step**2:
            image = self.drawImage(pokemons)

        self.callback(pokemons, image, self.current)

    def drawImage(self, pokemons):
        image = self.image.copy()
        for key, pokemon in pokemons.iteritems():
            self.drawPokemon(image, pokemon)

        return image

    def drawPokemon(self, image, pokemon):
        pokemonImage = Image \
            .open(utils.path(__file__, '../modules/PokemonGoMap/static/icons/' + str(pokemon['id']) + '.png')) \
            .convert('RGBA')

        offset = utils.buildOffset(
            point = Location.fromPokemonLocation(pokemon),
            center = self.location,
            size = consts.SIZE,
            zoom = consts.MAP['ZOOM'] - self.step
        )

        image.paste(
            pokemonImage,
            (
                offset[0] - pokemonImage.size[0] / 2,
                offset[1] - pokemonImage.size[1] / 2
            ),
            mask = pokemonImage
        )
