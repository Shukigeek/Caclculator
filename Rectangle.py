from calculator import Shape
class Rectangle(Shape):
    def __init__(self,side1,side2):
        super().__init__("Rectangle")
        self.side1 = side1
        self.side2 = side2
    def show_area(self):
        return self.side1 * self.side2
    def get_perimeter(self):
        return (self.side1 + self.side2) * 2

    def ascii_art(self):
        w = self.side1
        h = self.side2

        return f"""
    +{'-' * int(w)}+
    |{' ' * int(w)}|  h = {h}
    |{' ' * int(w)}|
    +{'-' * int(w)}+
      w = {w}
      
    Area: {self.show_area()}
    perimeter: {self.get_perimeter()}
    """
if __name__ == '__main__':

    d = Rectangle(12,3)
    print(d)