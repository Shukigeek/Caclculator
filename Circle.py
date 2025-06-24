from calculator import Shape
import math

class Circle(Shape):
    def __init__(self,radius):
        super().__init__("Circle")
        self.radius = radius
    def show_area(self):
        return math.pi * (self.radius**2)
    def get_perimeter(self):
        return 2 * math.pi * self.radius