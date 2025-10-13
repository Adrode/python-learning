# Losowa gra "RPG", do przećwiczenia OOP i klas.
# Wstępnie 3 rodzaje postaci do wyboru. Wybierasz 1 postać i walczysz przeciwko 2 pozostałym. 
# Każda postać ma pasek życia i zadeklarowany DMG.
# Różne postaci mają manę lub staminę, zależnie od rodzaju ataków.
# Każda postać ma 33% szansy na uniknięcie obrażen od przeciwnika.
# Każda postać ma własne właściwości co do zadawanych ataków.

from abc import ABC, abstractmethod
import time
import random

class Character(ABC):
  def __init__(self, name, damage, hp):
    self.name = name
    self.damage = damage
    self.hp = hp
    self.dodge_chance = 1

  @abstractmethod
  def attack(self, target):
    pass
      
  def hp_left(self):
    return f"{self.name} has {self.hp} HP left."

  def dodge(self):
    rand_number = random.randint(1, 3)

    if rand_number == self.dodge_chance:
      print(f"{self.name} has dodged the attack! 0 DMG dealt")
      return True
    else:
      return False

class Warrior(Character):
  def __init__(self, name, damage, hp):
    super().__init__(name, damage, hp)
    self.stamina = 30 # future usage

  def attack(self, target):
    print("Warrior's attack:")
    if not target.dodge() == True:
      target.hp -= self.damage
      print(f"{self.name} has dealt {self.damage} DMG to {target.name}. {target.hp_left()}")

class Mage(Character):
  def __init__(self, name, damage, hp):
    super().__init__(name, damage, hp)
    self.mana = 30 # future usage

  def attack(self, target):
    print("Mage's attack:")
    if not target.dodge() == True:
      target.hp -= self.damage
      print(f"{self.name} has dealt {self.damage} DMG to {target.name}. {target.hp_left()}")

class Rogue(Character):
  def __init__(self, name, damage, hp):
    super().__init__(name, damage, hp)
    self.stamina = 30 # future usage

  def attack(self, target):
    print("Rogue's attack:")
    if not target.dodge() == True:
      target.hp -= self.damage
      print(f"{self.name} has dealt {self.damage} DMG to {target.name}. {target.hp_left()}")


warrior = Warrior("Warrior", 10, 100)
mage = Mage("Mage", 20, 50)
rogue = Rogue("Rogue", 15, 75)

while warrior.hp > 0 and mage.hp > 0:
  warrior.attack(mage)
  if mage.hp <= 0:
    print("Mage is dead")
    break
  time.sleep(5)

  mage.attack(warrior)
  if warrior.hp <= 0:
    print("Warrior is dead")
    break
  time.sleep(5)