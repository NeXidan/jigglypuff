import requests

from PIL import Image

from libs import utils, consts
from libs.searcher import Searcher

from libs.geom.location import Location

class Map():
    def __init__(self, location, callback, step):
        self.location = Location.factory(location)
        self.step = step
        self.callback = callback

        locationString = self.location.toString()

        data = {
            'zoom': consts.MAP['ZOOM'],
            'center': locationString,
            'markers': locationString
        }

        data.update(consts.MAP['API']['PARAMS'])

        response = requests.get(consts.MAP['API']['URL'], data, stream=True)
        response.raw.decode_content = True
        self.image = Image.open(response.raw).convert('RGBA')

        Searcher(
            location = self.location,
            handler = self.handler,
            step = self.step
        ).search()


    def handler(self, pokemons, currSteps, totalSteps):
        image = None
        if currSteps == totalSteps:
            image = self.drawImage(pokemons)

        self.callback(pokemons, image, currSteps, totalSteps)

    def drawImage(self, pokemons):
        image = self.image.copy()
        for pokemon in pokemons:
            self.drawPokemon(image, pokemon)

        return image

    def drawPokemon(self, image, pokemon):
        pokemonImage = Image \
            .open(utils.path(__file__, '../modules/PokemonGoMap/static/icons/' + str(pokemon['id']) + '.png')) \
            .convert('RGBA')

        offset = utils.buildOffset(
            point = Location.factory(pokemon),
            center = self.location,
            size = consts.SIZE,
            zoom = consts.MAP['ZOOM']
        )

        image.paste(
            pokemonImage,
            (
                offset[0] - pokemonImage.size[0] / 2,
                offset[1] - pokemonImage.size[1] / 2
            ),
            mask = pokemonImage
        )
