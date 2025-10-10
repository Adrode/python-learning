from abc import ABC, abstractmethod
import math

class Shape(ABC):
  def __init__(self, a):
    self.a = a

  @abstractmethod
  def area(self):
    pass

class Square(Shape):
  def area(self):
    print(f"Square area: {self.a ** 2}")

class Circle(Shape):
  def area(self):
    print(f"Circle area: {round(2 * math.pi * self.a, 2)}")

square = Square(11)
circle = Circle(5)

square.area()
circle.area()