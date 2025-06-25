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

    def ascii_art(self):
        r = self.radius
        area = round(self.show_area(), 2)
        perimeter = round(self.get_perimeter(), 2)

        return f"""
        *  *
     *        *        
    *          *     radius: {r}
    *          *      
     *        *        
        *  *              

    Area: {area}
    Perimeter: {perimeter}
    """

if __name__ == '__main__':
    a = Circle(4)
    print(a)