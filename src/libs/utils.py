import os

def locationToString(location, separator = ','):
    return str(location['longitude']) + separator + str(location['latitude'])

def path(path):
    return os.path.join(os.path.dirname(__file__), '../../' + path)
