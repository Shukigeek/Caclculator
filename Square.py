from Rectangle import  Rectangle

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
        self.name  = "Square"
        self.side = side
    def get_perimeter(self):
        return self.side * 4

if __name__ == '__main__':

    a = Square(4)
    print(a)