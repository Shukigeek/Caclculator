from calculator import Shape
import  math

class Triangle(Shape):
    def __init__(self,a,b,c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c

        if (a + b <= c or a + c <= b or b + c <= a):
            raise ValueError("Invalid triangle: the side lengths do not satisfy the triangle inequality.")
    def show_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area
    def get_perimeter(self):
        return self.a + self.b + self.c
if __name__ == '__main__':
    a = Triangle(1,2,3)
    print(a)