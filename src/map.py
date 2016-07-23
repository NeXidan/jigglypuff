import requests

from PIL import Image

from libs import utils, consts
from libs.searcher import Searcher

from libs.geom.location import Location

class Map():
    def __init__(self, location, callback, zoom):
        self.location = Location.fromTelegramLocation(location)
        self.zoom = zoom
        self.callback = callback

        locationString = self.location.toString()

        data = {
            'zoom': zoom,
            'center': locationString,
            'markers': locationString
        }

        data.update(consts.MAP['API']['PARAMS'])

        response = requests.get(consts.MAP['API']['URL'], data, stream=True)
        response.raw.decode_content = True
        self.image = Image.open(response.raw).convert('RGBA')

        self.searcher = Searcher(
            location = self.location,
            callback = self.handler
        )

        self.searcher.call('register_background_thread', initial_registration=True)

    def handler(self):
        image = self.image.copy()

        pokemons = self.searcher.get('pokemons')
        for key, pokemon in pokemons.iteritems():
            self.drawPokemon(image, pokemon)

        self.callback(image)

    def drawPokemon(self, image, pokemon):
        pokemonImage = Image \
            .open(utils.path(__file__, '../modules/PokemonGoMap/static/icons/' + str(pokemon['id']) + '.png')) \
            .convert('RGBA')

        offset = utils.buildOffset(
            point = Location.fromPokemonLocation(pokemon),
            center = self.location,
            size = consts.SIZE,
            zoom = self.zoom
        )

        image.paste(
            pokemonImage,
            (
                offset[0] - pokemonImage.size[0] / 2,
                offset[1] - pokemonImage.size[1] / 2
            ),
            mask = pokemonImage
        )
