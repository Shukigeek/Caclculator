from calculator import Shape
import math

class RightTriangle(Shape):
    def __init__(self,base,height):
        super().__init__("RightTriangle")
        self.base = base
        self.height = height
    def show_area(self):
        return (self.base * self.height) / 2
    def get_perimeter(self):
        c = math.sqrt((self.base**2)+(self.height**2))
        return self.height + self.base + c

    def ascii_art(self):
        hypotenuse = round(math.sqrt(self.base ** 2 + self.height ** 2), 2)
        area = round(self.show_area(), 2)
        perimeter = round(self.get_perimeter(), 2)

        return f"""
            |\\
        {self.height:<3} | \\  
            |  \\
            |   \\ 
            |    \\  {hypotenuse}
            |     \\
            |______\\
               {self.base}

    Area: {area}
    Perimeter: {perimeter}
    """

if __name__ == '__main__':
    a = RightTriangle(2,900)
    print(a)