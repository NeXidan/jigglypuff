from __future__ import division
import math

from location import Location
from point import Point

MERCATOR_RANGE = 256
PIXEL_ORIGIN =  Point(MERCATOR_RANGE / 2, MERCATOR_RANGE / 2)
PIXELS_PER_LON_DEGREE = MERCATOR_RANGE / 360
PIXELS_PER_LON_RADIAN = MERCATOR_RANGE / (2 * math.pi)

def bound(value, optMin, optMax):
    if (optMin != None):
        value = max(value, optMin)
    if (optMax != None):
        value = min(value, optMax)
    return value

def degreesToRadians(deg):
    return deg * (math.pi / 180)

def radiansToDegrees(rad):
    return rad / (math.pi / 180)

class Projection:
    @staticmethod
    def fromLocationToPoint(location):
        siny = bound(math.sin(degreesToRadians(location.latitude)), -0.9999, 0.9999)

        return Point(
            PIXEL_ORIGIN.x + location.longitude * PIXELS_PER_LON_DEGREE,
            PIXEL_ORIGIN.y + 0.5 * math.log((1 + siny) / (1 - siny)) * -PIXELS_PER_LON_RADIAN
        )

    @staticmethod
    def fromPointToLocation(point) :
        latRadians = (point.y - PIXEL_ORIGIN.y) / -PIXELS_PER_LON_RADIAN

        return Location(
            radiansToDegrees(2 * math.atan(math.exp(latRadians)) - math.pi / 2),
            (point.x - PIXEL_ORIGIN.x) / PIXELS_PER_LON_DEGREE
        )
