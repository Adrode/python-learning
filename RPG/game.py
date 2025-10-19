# Warrior - 200HP, 40 armor, 15 DMG, 10% dodge
# Mage - 100HP, 10 DMG co turę przez 4 tury, 30 DMG, 20% dodge
# Rogue - 120HP, 50% crit. - 30% szany, 20 DMG, 40% dodge

from abc import ABC, abstractmethod
import random
import time

class Character(ABC):
  def __init__(self, name, hp, damage, dodge_chance):
    self.name = name
    self.hp = hp
    self.damage = damage
    self.dodge_chance = dodge_chance

  def dodge(self, target):
    dodge_chance_number = random.randint(0, 100)
    if dodge_chance_number in range(0, target.dodge_chance):
      return True
    else:
      return False
    
  @abstractmethod
  def take_damage(self, opponent):
    pass

  def attack(self, target):
    if self.dodge(target) != True:
      print(f"{self.__class__.__name__} {self.name} deals {self.damage} DMG to {target.__class__.__name__}: {target.name}.")
      target.take_damage(self)
      return True
    else:
      print(f"{self.__class__.__name__} {self.name} missed! No DMG dealt to {target.__class__.__name__}: {target.name}.")
      return False

  @abstractmethod
  def show_stats(self):
    print(f"{self.__class__.__name__}: {self.name}\nHP: {self.hp}\nDMG: {self.damage}\nDodge chance: {self.dodge_chance}")

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
    crit_chance_number = random.randint(0, 100)
    if crit_chance_number in range(0, self.crit_chance):
      return True
    else:
      return False

  def attack(self, target):
    if self.crit_attack_chance() == True:
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

warrior = Warrior("Gacek", 200, 15, 10, 40)
rogue = Rogue("Niecny Maniuś", 120, 20, 40, 50, 30)

counter = 0
while warrior.hp > 0 and rogue.hp > 0:
  counter += 1
  print(f"ROUND {counter}")
  for i in range(3, 0, -1):
    print(f"{i}...")
    time.sleep(1)
  print("\nSTART!")
  print("--------------------")
  time.sleep(2)

  warrior.attack(rogue)
  time.sleep(2)
  rogue.attack(warrior)
  time.sleep(2)