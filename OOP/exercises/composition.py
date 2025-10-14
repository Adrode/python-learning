class Engine:
  def __init__(self, horse_power):
    self.horse_power = horse_power

class Wheel:
  def __init__(self, size):
    self.size = size

class Car:
  def __init__(self, model, horse_power, size):
    self.model = model
    self.hp = Engine(horse_power)
    self.wheels = [Wheel(size) for wheel in range(4)]

  def print_info(self):
    print(f"{self.model}, {self.hp.horse_power}HP, {self.wheels[0].size}\"")

car = Car("Cruze", 120, 16)

car.print_info()