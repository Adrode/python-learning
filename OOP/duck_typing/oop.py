class Dog:
  def speak(self):
    return f"Woof!"
  
class Duck:
  def speak(self):
    return f"Quack!"

class Cat:
  def speak(self):
    return f"Meow!"

class RoboDog:
  def speak(self):
    return f"*electronic* Woof!"
  
class Car:
  def sound(self):
    return f"HONK!"
  
def make_it_speak(obj):
  if hasattr(obj, "speak"):
    print(obj.speak())
  else:
    print("This object can't speak")
  
animals = [Dog(), Duck(), Cat(), RoboDog(), Car()]
for animal in animals:
  make_it_speak(animal)