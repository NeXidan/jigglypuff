from argparse import Namespace

from geom.size import Size

BOT = {
    'TOKEN': '262782965:AAG4YwtGV7f8geaF9FMdsiLpKhvjaIGgEj8',

    'STICKER': u'BQADBAADtgQAAjZHEwABA70wjTd86fIC'
}

SIZE = Size(1280, 1280, 2)

MAP = {
    'API': {
        'URL': 'https://maps.googleapis.com/maps/api/staticmap',
        'PARAMS': {
            'size': SIZE.toString(),
            'scale': SIZE.scale
        }
    }
}

SEARCHER = {
    'ARGS': Namespace(
        DEBUG = True,
        ampm_clock = False,
        auth_service = 'ptc',
        auto_refresh = None,
        china = False,
        debug = False,
        display_gym = False,
        display_pokestop = False,
        ignore = None,
        locale = 'en',
        only = None,
        onlylure = False
    )
}
