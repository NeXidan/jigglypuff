import os
import requests

from PIL import Image
from StringIO import StringIO

from libs import utils
import consts

class Map():
    def __init__(self, location):
        self.location = location

        locationString = utils.locationToString(self.location)

        data = {
            'spn': '0.002,0.0015',
            'll': locationString,
            'pt': locationString + ',pm2rdm'
        }

        data.update(consts.MAP['API']['PARAMS'])

        response = requests.get(
            consts.MAP['API']['URL'],
            data
        )

        self.image = Image.open(StringIO(response.content))
