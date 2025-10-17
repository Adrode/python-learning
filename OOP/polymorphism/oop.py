from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def area(self):
    print(f"Area: {self.width * self.height}")

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
  
  def area(self):
    print(f"Area: {3.14 * self.radius ** 2}")

class Triangle(Shape):
  def __init__(self, base, height):
    self.base = base
    self.height = height
  
  def area(self):
    print(f"Area: {self.base * self.height * 0.5}")

shapes = [Rectangle(5, 10), Circle(4), Triangle(10, 6)]

for shape in shapes:
  shape.area()