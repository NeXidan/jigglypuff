class Size:
    def __init__(self, width, height, scale = 1):
        self.width = width
        self.height = height
        self.scale = scale

    def get_real_width(self):
        return self.width / self.scale

    def get_real_height(self):
        return self.height / self.scale

    def to_string(self, separator = 'x'):
        return str(self.get_real_width()) + separator + str(self.get_real_height())
