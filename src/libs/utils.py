import os
from pyproj import Proj, transform

def locationToString(location, separator = ',', googleWay = False):
    if googleWay:
        return str(location['latitude']) + separator + str(location['longitude'])

    return str(location['longitude']) + separator + str(location['latitude'])

def toLocation(longitude, latitude):
    return {
        'longitude': longitude,
        'latitude': latitude
    }

def buildOffset(point, box, size):
    mercBox = (toMerc(box[0]), toMerc(box[1]))
    spn = (abs(mercBox[0][0] - mercBox[1][0]), abs(mercBox[0][0] - mercBox[1][0]))

    mercPoint = toMerc(point)

    left = (size['width'] * (mercPoint[0] - mercBox[0][0])) / spn[0]
    top = (size['height'] * (mercBox[1][1] - mercPoint[1])) / spn[1]

    return (int(left), int(top))

def boxToString(box):
    return str(box[0]['longitude']) \
        + ',' + str(box[0]['latitude']) \
        + '~' + str(box[1]['longitude']) \
        + ',' + str(box[1]['latitude'])

def buildBox(center, spn):
    bottomLeft = toLocation(center['longitude'] - spn / 2, center['latitude'] - spn / 2)
    topRight = toLocation(center['longitude'] + spn / 2, center['latitude'] + spn / 2)

    return (bottomLeft, topRight)

def path(filePath, relativePath):
    return os.path.join(os.path.dirname(filePath), relativePath)

def override(oldMethod, newMethod):
    def overrideMethod(*kwargs):
        oldMethod(*kwargs)
        newMethod()

    return overrideMethod

lonlat = Proj(init="epsg:4326")
merc = Proj(proj="merc", ellps="WGS84")

def toMerc(point, googleCoords = False):
    ll = (point['longitude'], point['latitude'])
    return transform(lonlat, merc, *ll)
