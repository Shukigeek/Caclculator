from Square import Square
from Rectangle import Rectangle
from RightTriangle import RightTriangle
from Triangle import Triangle
from Circle import Circle
from Hexagon import Hexagon

def get_positive_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val > 0:
                return val
            print("enter a valid number")
        except ValueError:
            print("not a valid number, try agine")

def main():
    print("Welcome to area calculator\n\n"
          "pick a shape to calculate:\n"
          "1: square\n"
          "2: rectangle\n"
          "3: right triangle\n"
          "4: triangle\n"
          "5: circle\n"
          "6: hexagon")
    choice = input("enter your choice")

    result = None

    if choice == "1":
        side = get_positive_float("choose the length of the square sides")
        result = Square(side)
    elif choice == "2":
        side1 = get_positive_float("choose the length of the first rectangle side")
        side2 = get_positive_float("choose the length of the second rectangle side")
        result = Rectangle(side1,side2)
    elif choice == "3":
        base = get_positive_float("choose the length of the triangle base")
        height = get_positive_float("choose the length of the triangle height")
        result = RightTriangle(base,height)
    elif choice == "4":
        try:
            a = get_positive_float("choose the length of the 'a' side")
            b = get_positive_float("choose the length of the 'b' side")
            c = get_positive_float("choose the length of the 'c' side")
            result = Triangle(a, b, c)
        except ValueError as ve:
            print(f"Error {ve}")
            return
    elif choice == "5":
        radius = get_positive_float("choose the length of the circle radius")
        result = Circle(radius)
    elif choice == "6":
        side = get_positive_float("choose the length of the one of hexagon side")
        result = Hexagon(side)
    else:
        print("not a valid choice")
        return
    print(result)


if __name__ == '__main__':
    main()