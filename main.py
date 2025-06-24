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

shape_classes = {
    "1": Square,
    "2": Rectangle,
    "3": RightTriangle,
    "4": Triangle,
    "5": Circle,
    "6": Hexagon,
}
def create_shape(choice):
    cls = shape_classes.get(choice)
    if not cls:
        print("Invalid choice")
        return None


    if cls in [Square, Hexagon]:
        side = get_positive_float("Enter the side length: ")
        return cls(side)
    elif cls == Rectangle:
        side1 = get_positive_float("Enter first side length: ")
        side2 = get_positive_float("Enter second side length: ")
        return cls(side1, side2)
    elif cls == RightTriangle:
        base = get_positive_float("Enter base length: ")
        height = get_positive_float("Enter height length: ")
        return cls(base, height)
    elif cls == Triangle:
        a = get_positive_float("Enter side a: ")
        b = get_positive_float("Enter side b: ")
        c = get_positive_float("Enter side c: ")
        try:
            return cls(a, b, c)
        except ValueError as ve:
            print(f"Error: {ve}")
            return None
    elif cls == Circle:
        radius = get_positive_float("Enter radius: ")
        return cls(radius)
def main():
    print("Welcome to area calculator\n\n"
          "pick a shape to calculate:\n"
          "1: square\n"
          "2: rectangle\n"
          "3: right triangle\n"
          "4: triangle\n"
          "5: circle\n"
          "6: hexagon\n\n"
          "special methods !!!!\n"
          "7: check 2 different shapes if they are area equal\n"
          "8: check 2 different shapes one is smaller than other\n"
          "9: add to shapes together and get the new area\n")

    choice = input("Enter your choice: ")

    if choice in shape_classes:
        shape = create_shape(choice)
        if shape:
            print(shape)

    elif choice in ["7", "8", "9"]:
        print("enter first shape:")
        menu = ("Choose shape number: \n1: square\n2: rectangle\n3: right triangle\n"
                "4: triangle\n5: circle\n6: hexagon\n")
        pick1 = input(menu)
        l = ["1", "2", "3", "4", "5", "6"]
        if not pick1 or pick1 not in l:
            print("invalid choice")
            return
        shape1 = create_shape(pick1)


        print("enter second shape:")
        pick2 = input(menu)
        if not pick2 or pick2 not in l:
            print("invalid choice")
            return
        shape2 = create_shape(pick2)


        if choice == "7":
            print(f"Are areas equal? {shape1 == shape2}")
        elif choice == "8":
            print(f"Is first shape smaller than second? {shape1 < shape2}")
        elif choice == "9":
            total_area = shape1 + shape2
            print(f"Total area: {total_area:.2f}")

    else:
        print("Not a valid choice")


if __name__ == '__main__':
    main()
