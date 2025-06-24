from calculator import Shape
import  math

class Triangle(Shape):
    def __init__(self,a,b,c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c
    def show_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area
if __name__ == '__main__':
    a = Triangle(5,3,4)
    print(a)