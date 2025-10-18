class MathOperations:
  @staticmethod
  def add(a, b):
    return a + b
  
  @staticmethod
  def subtract(a, b):
    return a - b
  
  @staticmethod
  def multiply(a, b):
    return a * b
  
  @staticmethod
  def divide(a, b):
    if b == 0:
      return f"Don't divide with 0"
    else:
      return a / b
    
  @staticmethod
  def description():
    return f"This class provides basic mathematical operations."
  

print(MathOperations.add(5, 5))
print(MathOperations.subtract(5, 10))
print(MathOperations.multiply(5, 3))
print(MathOperations.divide(5, 2))
print(MathOperations.divide(5, 0))
print(MathOperations.divide(0, 2))
print(MathOperations.description())