from argparse import Namespace

BOT = {
    'TOKEN': '262782965:AAG4YwtGV7f8geaF9FMdsiLpKhvjaIGgEj8',

    'STICKER': u'BQADBAADtgQAAjZHEwABA70wjTd86fIC'
}

SIZE = {
    'width': 450,
    'height': 450
}

MAP = {
    'API': {
        'URL': 'https://static-maps.yandex.ru/1.x/',
        'PARAMS': {
            'l': 'map',
            'lang': 'en_US',
            'size': str(SIZE['width']) + ',' + str(SIZE['height'])
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
