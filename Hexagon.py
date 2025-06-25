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

    def ascii_art(self):
        s = self.side
        area = round(self.show_area(), 2)
        perimeter = round(self.get_perimeter(), 2)

        return f"""
       ____   
      /    \\  
     /      \\ 
     \\      /   side = {s}
      \\____/  

    Area: {area}
    Perimeter: {perimeter}
    """
if __name__ == '__main__':
    a = Hexagon(3)
    print(a)