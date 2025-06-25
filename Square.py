from Rectangle import  Rectangle
import turtle

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
        self.name  = "Square"
        self.side = side
    def get_perimeter(self):
        return self.side * 4

    def ascii_art(self):
        s = str(self.side)
        p = self.get_perimeter()
        return f"""
         {s}
        --------
        |      |
    {s} |      | {s}
        --------
         {s}

    Perimeter: {p}
    Area: {self.show_area()}
    """



if __name__ == '__main__':

    a = Square(4)
    print(a)