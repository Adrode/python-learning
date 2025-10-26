# Warrior - 200HP, 15 DMG, 10% dodge, 40 armor
# Knight - 180HP, 20 DMG, 10% dodge, 30 armor, 50% bonus crit. - 50% hit chance
# Mage - 100HP, 30 DMG, 20% dodge, 10 DOT - 2 tury - 30% hit chance
# Rogue - 120HP, 20 DMG, 40% dodge, 75% bonus crit. - 30% hit chance
# Gunman - 100HP, 30DMG, 30% dodge, 20 DOT - 2 tury - 20% hit chance, 100% bonus crit. - 50% hit chance

# Warrior BONUS: armor, który po zejściu do wartości 0 "pęka", ale nie przepuszcza w tej turze kolejnych obrażeń przeciwnika
# Knight BONUS: tak jak Warrior
# Rogue BONUS: losowa szansa na zadanie critical damage
# Mage BONUS: nałożenie efektu DOT (damage over time), który zadaje obrażenia od tej samej tury;
#             efekt może się multiplikować (jednocześnie może zostać nałożone wiele razy ten sam efekt, ale każdy ma swoją liczbę tur, w której obowiązuje)
# Gunman BONUS: tak jak Mage, DOT + HasCRIT

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
  def take_damage(self, opponent_damage):
    pass

  def attack(self, target):
    if not self.dodge(target):
      print(f"{self.__class__.__name__} '{self.name}': deals {self.damage} DMG to {target.__class__.__name__}: '{target.name}'.")
      print(target.take_damage(self.damage))
    else:
      print(f"{self.__class__.__name__} '{self.name}': missed! No DMG dealt to {target.__class__.__name__}: '{target.name}'.")

  @abstractmethod
  def show_stats(self):
    print(f"{self.__class__.__name__} '{self.name}'")
    print(f"HP: {self.hp}")
    print(f"DMG: {self.damage}")
    print(f"Dodge chance: {self.dodge_chance}%")

class HasCRIT:
  def __init__(self, crit_value, crit_chance, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.crit_value = crit_value
    self.crit_chance = crit_chance

  def crit_attack_chance(self):
    return random.random() < self.crit_chance / 100

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
      print(f"{self.__class__.__name__} '{self.name}': applied DOT to enemy! Number of currently applied effects: {len(self.dot_counters)}") # tutaj do poprawki, bo podliczanie się pierdoli

  def deal_dot(self, target):
    temp_sum = 0
    for key, value in list(self.dot_counters.items()):
      if value > 0:
        temp_sum += self.damage_over_time
        self.dot_counters.update({key: value - 1})
    if temp_sum:
        print(f"{self.__class__.__name__} '{self.name}': deals {temp_sum} DMG as DOT to {target.__class__.__name__}: {target.name}.")
        print(target.take_damage(temp_sum))

class Warrior(Character):
  def __init__(self, name, hp, damage, dodge_chance, armor, *args, **kwargs):
    super().__init__(name, hp, damage, dodge_chance, *args, **kwargs)
    self.armor = armor

  def show_stats(self):
    super().show_stats()
    print(f"Armor: {self.armor}")

  def attack(self, target):
    super().attack(target)
  
  def take_damage(self, opponent_damage):
    if self.armor >= 0:
      self.armor -= opponent_damage
      if self.armor <= 0:
        return f"{self.__class__.__name__} '{self.name}': {self.hp} HP left, armor broken"
      else:
        return f"{self.__class__.__name__} '{self.name}': {self.hp} HP left, {self.armor} armor left"
    else:
      self.hp -= opponent_damage
      if self.hp < 0:
        self.hp = 0
      return f"{self.__class__.__name__} '{self.name}': {self.hp} HP left"
    
class Knight(Warrior, HasCRIT):
  def __init__(self, name, hp, damage, dodge_chance, armor, crit_value, crit_chance, *args, **kwargs):
    super().__init__(name, hp, damage, dodge_chance, armor, crit_value, crit_chance, *args, **kwargs)

  def show_stats(self):
    super().show_stats()
    print(f"Crit value: {self.crit_value}")
    print(f"Crit chance: {self.crit_chance}%")

  def attack(self, target):
    if super().crit_attack_chance():
      print("CRITICAL!")
      temp_damage = self.damage
      self.damage *= (self.crit_value / 100) + 1
      super().attack(target)
      self.damage = temp_damage
    else:
      super().attack(target)

class Rogue(Character, HasCRIT):
  def __init__(self, name, hp, damage, dodge_chance, crit_value, crit_chance, *args, **kwargs):
    super().__init__(name, hp, damage, dodge_chance, crit_value, crit_chance, *args, **kwargs)

  def show_stats(self):
    super().show_stats()
    print(f"Crit value: {self.crit_value}")
    print(f"Crit chance: {self.crit_chance}%")

  def attack(self, target):
    if super().crit_attack_chance():
      print("CRITICAL!")
      temp_damage = self.damage
      self.damage *= (self.crit_value / 100) + 1
      super().attack(target)
      self.damage = temp_damage
    else:
      super().attack(target)
  
  def take_damage(self, opponent_damage):
    self.hp -= opponent_damage
    if self.hp < 0:
      self.hp = 0
    return f"{self.__class__.__name__} '{self.name}': {self.hp} HP left"

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
    print(f"DOT apply chance: {self.chance_dot}%")

  def attack(self, target):
    if not self.dodge(target):
      print(f"{self.__class__.__name__} '{self.name}' deals {self.damage} DMG to {target.__class__.__name__}: {target.name}.")
      self.initiate_dot()
      print(target.take_damage(self.damage))
      self.deal_dot(target)
    else:
      self.deal_dot(target)
      print(f"{self.__class__.__name__} {self.name} missed! No DMG dealt to {target.__class__.__name__}: {target.name}.")

  def take_damage(self, opponent_damage):
    self.hp -= opponent_damage
    if self.hp < 0:
      self.hp = 0
    return f"{self.__class__.__name__} '{self.name}': {self.hp} HP left"
  
class Gunman(Mage, HasCRIT):
  def __init__(self, name, hp, damage, dodge_chance, damage_over_time, num_rounds_dot, chance_dot, crit_value, crit_chance, *args, **kwargs):
    super().__init__(name, hp, damage, dodge_chance, damage_over_time, num_rounds_dot, chance_dot, crit_value, crit_chance, *args, **kwargs)

  def show_stats(self):
    super().show_stats()
    print(f"Crit value: {self.crit_value}")
    print(f"Crit chance: {self.crit_chance}%")
  
  def attack(self, target):
    if not self.dodge(target):
      if super().crit_attack_chance():
        print("CRITICAL!")
        temp_damage = self.damage
        self.damage *= (self.crit_value / 100) + 1
        print(f"{self.__class__.__name__} '{self.name}' deals {self.damage} DMG to {target.__class__.__name__}: {target.name}.")
        print(target.take_damage(self.damage))
        self.damage = temp_damage
      else:
        print(f"{self.__class__.__name__} '{self.name}' deals {self.damage} DMG to {target.__class__.__name__}: {target.name}.")
        print(target.take_damage(self.damage))
      self.initiate_dot()
      self.deal_dot(target)
    else:
      self.deal_dot(target)
      print(f"{self.__class__.__name__} {self.name} missed! No DMG dealt to {target.__class__.__name__}: {target.name}.")

warrior = Warrior("Waruś", 200, 15, 10, 40)
knight = Knight("Rycerzyk Henryk", 180, 20, 10, 30, 50, 50)
rogue = Rogue("Niecny Maniuś", 120, 20, 40, 75, 30)
mage = Mage("Czarujący Czarek", 100, 30, 20, 10, 2, 30)
gunman = Gunman("Strzelczyk Szczepan", 100, 30, 30, 20, 2, 20, 100, 50)

all_characters = [warrior, knight, rogue, mage, gunman]

def show_all_stats():
  for character in all_characters:
    character.show_stats()
    print("----------")

print("Welcome to Brightest Sanctuary!")
while True:
  menu = input("[1] Show statistics of all characters\n[2] Start game\n")
  if menu not in '12':
    print("Wrong number typed. Choose again")
    continue
  match menu:
    case '1':
      show_all_stats()
    case '2':
      break

choose_character = '0'
while choose_character not in '12345':
  choose_character = input("Choose you character:\n[1] Warrior\n[2] Rogue\n[3] Mage\n[4] Knight\n[5] Gunman\n")
  match choose_character:
    case '1':
      player = warrior
    case '2':
      player = rogue
    case '3':
      player = mage
    case '4':
      player = knight
    case '5':
      player = gunman
    case _:
      print("Wrong number typed. Choose again.")

while True:
  random_enemy = str(random.randint(1, 6))
  if random_enemy == choose_character:
    continue
  match random_enemy:
    case '1':
      enemy = warrior
      break
    case '2':
      enemy = rogue
      break
    case '3':
      enemy = mage
      break
    case '4':
      enemy = knight
      break
    case '5':
      player = gunman
      break

print(f"{player.__class__.__name__}: {player.name} VS. {enemy.__class__.__name__}: {enemy.name}")

counter = 0
while player.hp > 0 and enemy.hp > 0:
  counter += 1
  print(f"ROUND {counter}")
  for i in range(3, 0, -1):
    print(f"{i}...")
    time.sleep(1)
  print("\nSTART!")
  print("--------------------")
  time.sleep(2)
  if player.hp > 0: 
    player.attack(enemy)
    if enemy.hp <= 0:
      print(f"{player.__class__.__name__} won! You won!")
      break
  time.sleep(2)
  if enemy.hp > 0:
    enemy.attack(player)
    if player.hp <= 0:
      print(f"{enemy.__class__.__name__} won! Enemy won!")
      break
  time.sleep(2)