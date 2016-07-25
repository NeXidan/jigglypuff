from __future__ import division
import math

from location import Location
from point import Point

MERCATOR_RANGE = 256
PIXEL_ORIGIN =  Point(MERCATOR_RANGE / 2, MERCATOR_RANGE / 2)
PIXELS_PER_LON_DEGREE = MERCATOR_RANGE / 360
PIXELS_PER_LON_RADIAN = MERCATOR_RANGE / (2 * math.pi)

def bound(value, opt_min, opt_max):
    if (opt_min != None):
        value = max(value, opt_min)
    if (opt_max != None):
        value = min(value, opt_max)
    return value

def degrees_to_radians(deg):
    return deg * (math.pi / 180)

def radians_to_degrees(rad):
    return rad / (math.pi / 180)

class Projection:
    @staticmethod
    def from_location_to_point(location):
        siny = bound(math.sin(degrees_to_radians(location.latitude)), -0.9999, 0.9999)

        return Point(
            PIXEL_ORIGIN.x + location.longitude * PIXELS_PER_LON_DEGREE,
            PIXEL_ORIGIN.y + 0.5 * math.log((1 + siny) / (1 - siny)) * -PIXELS_PER_LON_RADIAN
        )

    @staticmethod
    def from_point_to_location(point) :
        latRadians = (point.y - PIXEL_ORIGIN.y) / -PIXELS_PER_LON_RADIAN

        return Location(
            radians_to_degrees(2 * math.atan(math.exp(latRadians)) - math.pi / 2),
            (point.x - PIXEL_ORIGIN.x) / PIXELS_PER_LON_DEGREE
        )
