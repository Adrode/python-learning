class Animal:
  def eat(self):
    print(f"{self.name} is eating")

class Prey(Animal):
  def flee(self):
    print(f"{self.name} is running away!")

class Predator(Animal):
  def hunt(self):
    print(f"{self.name} is hunting")

class Rabbit(Prey):
  pass

class Eagle(Predator):
  pass

class Fish(Prey, Predator):
  def __init__(self, name):
    self.name = name

fish = Fish("Tony")

fish.hunt()

class Small_fish(Fish):
  def quick_dodge(self):
    print("Damn! Little fish is doding quick!")

fish2 = Small_fish("Little Tony")

fish2.flee()
fish2.quick_dodge()
fish.eat()