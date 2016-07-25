from __future__ import division
import os
import argparse

from geom.point import Point
from geom.merc import Projection

def build_offset(point, center, size, zoom):
    scale = 2**zoom

    point = Projection.from_location_to_point(point)
    center = Projection.from_location_to_point(center)
    corner = Point(
        center.x - (size.get_real_width() / 2) / scale,
        center.y + (size.get_real_height() / 2) / scale
    )

    spn = (2 * abs(center.x - corner.x), 2 * abs(center.y - corner.y));

    left = (size.width * (point.x - corner.x)) / spn[0]
    top = (size.height * (point.y - corner.y + spn[1])) / spn[1]

    return (int(left), int(top))

def path(filePath, relativePath):
    return os.path.join(os.path.dirname(filePath), relativePath)
