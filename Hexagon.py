from calculator import Shape
import math

class Hexagon(Shape):
    def __init__(self,side):
        super().__init__("Hexagon")
        self.side = side
    def show_area(self):
        return ((3 * math.sqrt(3)) / 2) * (self.side**2)
    def get_perimeter(self):
        return self.side * 6
if __name__ == '__main__':
    a = Hexagon(3)
    print(a)