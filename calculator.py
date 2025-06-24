from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def show_area(self):
        pass
    def __str__(self):
        return f"{self.name} with the area of: {self.show_area():.2f}"