import random

class Animal:
  def __init__(self, name):
    self.name = name
    self.is_alive = True
    self.rand_time = random.randrange(1, 24)

  def eat(self):
    print(f"{self.name} is eating")

  def sleep(self):
    print(f"{self.name} has been sleeping for {self.rand_time} hours")

class Dog(Animal):
  def speak(self):
    print("BARK BARK!")

class Cat(Animal):
  def speak(self):
    print("MEOW!")

dog = Dog("Jupik")
cat = Cat("Jerry")

cat.sleep()
dog.sleep()

cat.speak()
dog.speak()