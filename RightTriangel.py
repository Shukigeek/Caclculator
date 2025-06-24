from calculator import Shape

class RightTriangle(Shape):
    def __init__(self,base,height):
        super().__init__("RightTriangle")
        self.base = base
        self.height = height
    def show_area(self):
        return (self.base * self.height) / 2

if __name__ == '__main__':
    a = RightTriangle(2,9)
    print(a)