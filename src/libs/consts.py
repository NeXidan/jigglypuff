from geom.size import Size

BOT = {
    'TOKEN': '262782965:AAG4YwtGV7f8geaF9FMdsiLpKhvjaIGgEj8',

    'STICKER': u'BQADBAADtgQAAjZHEwABA70wjTd86fIC',

    'LOCATION': {
        'REPLY': '*Jigglypuff* is searching:  `%d / %d`'
    },

    'KEYBOARD': {
        'SHOW': {
            'keyboard': [
                [{
                    'text': 'Send your location',
                    'request_location': True
                }]
            ],
            'resize_keyboard': True
        },
        'HIDE': {
            'hide_keyboard': True
        }
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

HELP_MESSAGE = 'Hello, young trainer. My name is *Jigglypuff* and i would like to help u locate all pokemons near u. Here i would like to answer some quations.Let\'s start\n\n*1*.How i can recieve pokemon\'s location?:\nYou should send your lacation from media selection\n*2*.Why my perfomance is very poor?:\nCause the machine, that my master use, has a poor perfomance too.\n*3*.I sent my location, but progress still on 0. What happend?:\nProbably, Pokemon\'s servers are down,u should wait for some minutes or hours.\n*4*.When searching is over, i didn\'t get a map. Why?:\nProbably, your district is down, launch a game and check, for any pokestops and "Nearby" sceen. If u can\'t see them, there is a answer.\n\nSo, I hope u will enjoy my work and u will catch all pokemons, Good luck!!!\n\n[Source code](https://github.com/NeXidan/jigglypuff)'
