class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def toString(self, separator = ','):
        return str(self.latitude) + separator + str(self.longitude)

    @staticmethod
    def factory(location):
        return Location(location['latitude'], location['longitude'])
