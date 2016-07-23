class Size:
    def __init__(self, width, height, scale = 1):
        self.width = width
        self.height = height
        self.scale = scale

    def getRealWidth(self):
        return self.width / self.scale

    def getRealHeight(self):
        return self.height / self.scale

    def toString(self, separator = 'x'):
        return str(self.getRealWidth()) + separator + str(self.getRealHeight())
