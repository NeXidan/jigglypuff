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
    },

    'HELP': '''
Hello, young trainer. I'm *Jigglypuff*, `Pokemon GO` helper pokebot!

*Jigglypuff* accepts:
    /start - starts interaction with pokebot
    /help - shows help reference
    /stop - stops current activity
    /keyboard - shows keyboard

Quick FAQ from *Jigglypuff*:

*Q:* How i can see pokemons nearby?
*A:* Just send *Jigglypuff* your location through attach media!

*Q:* *Jigglypuff* is too slow! Bad pokebot!
*A:* *Jigglypuff* is so sorry. My master's hardware is poor. Sometimes he puts me in a small raspberry box.

*Q:* Searching progress is on zero. Wtf, pokebot?
*A:* *Jigglypuff* don't know. Maybe Pokemon GO servers are down, or i'm down. Please, try later.

*Q:* I get map without pokemons! I came here to cheat, you dummy pokebot.
*A:* Maybe your district is laggy? Launch game and check for any activities around you and `Nearby` screen.

Catch em all! See ya, trainer!

[Jigglypuff share link](http://telegram.me/jigglypuffbot)
[Jigglypuff on github](https://github.com/NeXidan/jigglypuff)
    '''
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
