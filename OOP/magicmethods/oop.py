import math

class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"Vector({self.x}, {self.y})"
  
  def __repr__(self):
    return f"{self.__class__.__name__}(x={self.x}, y={self.y})"
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)
  
  def __len__(self):
    return len([self.x, self.y])
  
  def magnitude(self):
    return round(math.sqrt(self.x ** 2 + self.y ** 2), 2)

v1 = Vector2D(3, 4)
v2 = Vector2D(3, 6)
print(v1)
print(v1 == v2)
print(v1 + v2)
print(len(v1))
print(v2.magnitude())