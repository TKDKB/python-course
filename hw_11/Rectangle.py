class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def str(self):
        return f"Прямоугольник с высотой {height} и шириной {width}"

    @getter
    def get_area(self):
        return self.width * self.height

    @getter
    def get_perimetr(self):
        return (self.width + self.height) * 2

    @property
    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False