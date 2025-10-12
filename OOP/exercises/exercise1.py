from abc import ABC, abstractmethod

class Character(ABC):
  def __init__(self, name, dmg, hp):
    self.name = name
    self.dmg = dmg
    self.hp = hp

  @abstractmethod
  def attack(self):
    pass

  def take_dmg(self, dmg):
    self.hp -= dmg
    print(f"{self.name}: {dmg} DMG taken. {self.hp} HP left")

class Warrior(Character):
  def __init__(self):
    super().__init__(name = "Warrior", dmg = 10, hp = 100)

  def attack(self, target):
    print(f"{self.name}: {self.dmg} dealt to {target.name}.")
    target.take_dmg(self.dmg)
    
class Mage(Character):
  def __init__(self):
    super().__init__(name = "Mage", dmg = 20, hp = 50)

  def attack(self, target):
    print(f"{self.name}: {self.dmg} dealt to {target.name}.")
    target.take_dmg(self.dmg)

class Knight(Warrior):
  def __init__(self):
    super().__init__()
    self.name = "Knight"

  def attack(self, target):
    print(f"{self.name}: {self.dmg + 10} dealt to {target.name}.")
    target.take_dmg(self.dmg)

warrior = Warrior()
mage = Mage()
knight = Knight()

warrior.attack(mage)
knight.attack(mage)
warrior.attack(mage)
knight.attack(mage)
warrior.attack(mage)
knight.attack(mage)
