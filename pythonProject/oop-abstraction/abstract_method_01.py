from abc import ABC, abstractmethod


class Shape(ABC):

    def execute(self):
        print("Calculating area...")
        self.area()

    def sum(self, a, b):
        c = a + b
        return c

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return print(self.length * self.width)


#
# # Example usage
r = Rectangle(5, 10)
r.execute()
# # Polymorphism: Shape type reference holding Rectangle object
# shape: Shape = Rectangle(5, 10)
# shape.execute()
