from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def show_area(self):
        pass
    @abstractmethod
    def get_perimeter(self):
        pass
    @abstractmethod
    def ascii_art(self):
        pass
    def __str__(self):
        return f"{self.name} with the area of: {self.show_area():.2f} and a perimeter of: {self.get_perimeter():.2f}\n{self.ascii_art()}"



    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __eq__(self, other):
        return isinstance(other, Shape) and self.show_area() == other.show_area()

    def __lt__(self, other):
        return isinstance(other, Shape) and self.show_area() < other.show_area()

    def __add__(self, other):
        if isinstance(other, Shape):
            return self.show_area() + other.show_area()
        return NotImplemented