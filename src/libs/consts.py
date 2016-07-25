from geom.size import Size

BOT = {
    'TOKEN': '262782965:AAG4YwtGV7f8geaF9FMdsiLpKhvjaIGgEj8',

    'STICKER': u'BQADBAADtgQAAjZHEwABA70wjTd86fIC',

    'LOCATION': {
        'REPLY': '*Jigglypuff* is searching:  `%d / %d`'
    }
}

SIZE = Size(1280, 1280, 2)

MAP = {
    'API': {
        'URL': 'https://maps.googleapis.com/maps/api/staticmap',
        'PARAMS': {
            'size': SIZE.to_string(),
            'scale': SIZE.scale
        }
    },

    'ZOOM': 15
}
