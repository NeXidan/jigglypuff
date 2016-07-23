from __future__ import division
import os

from geom.point import Point
from geom.merc import Projection

def buildOffset(point, center, size, zoom):
    scale = 2**zoom

    point = Projection.fromLocationToPoint(point)
    center = Projection.fromLocationToPoint(center)
    corner = Point(
        center.x - (size.getRealWidth() / 2) / scale,
        center.y + (size.getRealHeight() / 2) / scale
    )

    spn = (2 * abs(center.x - corner.x), 2 * abs(center.y - corner.y));

    left = (size.width * (point.x - corner.x)) / spn[0]
    top = (size.height * (point.y - corner.y + spn[1])) / spn[1]

    return (int(left), int(top))

def path(filePath, relativePath):
    return os.path.join(os.path.dirname(filePath), relativePath)

def override(oldMethod, newMethod):
    def overrideMethod(*kwargs):
        oldMethod(*kwargs)
        newMethod()

    return overrideMethod
