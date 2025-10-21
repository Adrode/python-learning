# Warrior - 200HP, 40 armor, 15 DMG, 10% dodge
# Mage - 100HP, 10 DMG co turę przez 2 tury - 40% chance, 30 DMG, 20% dodge
# Rogue - 120HP, 50% crit. - 30% szany, 20 DMG, 40% dodge

from abc import ABC, abstractmethod
import random
import time

class Character(ABC):
  def __init__(self, name, hp, damage, dodge_chance, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.name = name
    self.hp = hp
    self.damage = damage
    self.dodge_chance = dodge_chance

  def dodge(self, target):
    return random.random() < target.dodge_chance / 100
    
  @abstractmethod
  def take_damage(self, opponent):
    pass

  def attack(self, target):
    if not self.dodge(target):
      print(f"{self.__class__.__name__} {self.name} deals {self.damage} DMG to {target.__class__.__name__}: {target.name}.")
      target.take_damage(self)
      return True
    else:
      print(f"{self.__class__.__name__} {self.name} missed! No DMG dealt to {target.__class__.__name__}: {target.name}.")
      return False

  @abstractmethod
  def show_stats(self):
    print(f"{self.__class__.__name__}: {self.name}\nHP: {self.hp}\nDMG: {self.damage}\nDodge chance: {self.dodge_chance}")

class HasDOT:
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.base_dot_counter = 0
    self.dot_counters = {}

  def chance_dot_counter(self):
    return random.random() < self.chance_dot / 100

  def generate_dot_counter(self):
    self.base_dot_counter += 1
    self.dot_counters.update({f"dot_counter{self.base_dot_counter}": self.num_rounds_dot})

  def initiate_dot(self):
    if self.chance_dot_counter():
      self.generate_dot_counter()

  def deal_dot(self, target):
    self.initiate_dot()
    temp_sum = 0
    for key, value in self.dot_counters.items():
      if value > 0:
        temp_sum += self.damage_over_time
        target.hp -= self.damage_over_time
        self.dot_counters.update({key: value - 1})
    if temp_sum:
      print(f"{self.__class__.__name__} {self.name} deals {temp_sum} DMG as DOT to {target.__class__.__name__}: {target.name}.")


class Warrior(Character):
  def __init__(self, name, hp, damage, dodge_chance, armor):
    super().__init__(name, hp, damage, dodge_chance)
    self.armor = armor

  def show_stats(self):
    super().show_stats()
    print(f"Armor: {self.armor}")

  def attack(self, target):
    super().attack(target)
  
  def take_damage(self, opponent):
    if self.armor >= 0:
      self.armor -= opponent.damage
      if self.armor <= 0:
        print(f"Warrior '{self.name}': {self.hp} HP left, armor broken")
      else:
        print(f"Warrior '{self.name}': {self.hp} HP left, {self.armor} armor left")
    else:
      self.hp -= opponent.damage
      print(f"Warrior '{self.name}': {self.hp} HP left")

class Rogue(Character):
  def __init__(self, name, hp, damage, dodge_chance, crit_value, crit_chance):
    super().__init__(name, hp, damage, dodge_chance)
    self.crit_value = crit_value
    self.crit_chance = crit_chance

  def show_stats(self):
    super().show_stats()
    print(f"Crit value: {self.crit_value}")
    print(f"Crit chance: {self.crit_chance}")

  def crit_attack_chance(self):
    return random.random() < self.crit_chance / 100

  def attack(self, target):
    if self.crit_attack_chance():
      print("CRITICAL!")
      temp_damage = self.damage
      self.damage *= (self.crit_value / 100) + 1
      super().attack(target)
      self.damage = temp_damage
    else:
      super().attack(target)
  
  def take_damage(self, opponent):
    self.hp -= opponent.damage
    print(f"Rogue '{self.name}': {self.hp} HP left")

class Mage(Character, HasDOT):
  def __init__(self, name, hp, damage, dodge_chance, damage_over_time, num_rounds_dot, chance_dot, *args, **kwargs):
    super().__init__(name, hp, damage, dodge_chance, *args, **kwargs)
    self.damage_over_time = damage_over_time
    self.num_rounds_dot = num_rounds_dot
    self.chance_dot = chance_dot

  def show_stats(self):
    super().show_stats()
    print(f"Damage over time: {self.damage_over_time}")
    print(f"No. of rounds for DOT: {self.num_rounds_dot}")
    print(f"DOT apply chance: {self.chance_dot}")

  def attack(self, target):
    super().attack(target)
    self.deal_dot(target)
  
  def take_damage(self, opponent):
    self.hp -= opponent.damage
    print(f"Mage '{self.name}': {self.hp} HP left")

warrior = Warrior("Gacek", 200, 15, 10, 40)
rogue = Rogue("Niecny Maniuś", 120, 20, 40, 50, 30)
mage = Mage("Czarujący Czarek", 100, 30, 20, 10, 4, 40)

counter = 0
while rogue.hp > 0 and mage.hp > 0:
  counter += 1
  print(f"ROUND {counter}")
  for i in range(3, 0, -1):
    print(f"{i}...")
    time.sleep(1)
  print("\nSTART!")
  print("--------------------")
  time.sleep(2)

  rogue.attack(mage)
  time.sleep(2)
  mage.attack(rogue)
  time.sleep(2)