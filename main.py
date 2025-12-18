class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        area = self.length * self.width
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
