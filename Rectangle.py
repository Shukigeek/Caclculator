from calculator import Shape
class Rectangle(Shape):
    def __init__(self,side1,side2):
        super().__init__("Rectangle")
        self.side1 = side1
        self.side2 = side2
    def show_area(self):
        return self.side1 * self.side2
if __name__ == '__main__':

    d = Rectangle(12,3)
    print(d)