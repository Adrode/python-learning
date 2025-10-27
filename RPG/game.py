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

class Item:
  def __init__(self, item_name, bonus_hp = None, bonus_damage = None):
    self.item_name = item_name
    self.bonus_hp = bonus_hp
    self.bonus_damage = bonus_damage

  def __str__(self):
    if self.bonus_hp:
      return f"{self.item_name}: +{self.bonus_hp} HP"
    elif self.bonus_damage:
      return f"{self.item_name}: +{self.bonus_damage} DMG"

class Character(ABC):
  all_characters = []

  def __init__(self, name, hp, damage, dodge_chance,*args, **kwargs):
    super().__init__(*args, **kwargs)
    self.name = name
    self.hp = hp
    self.damage = damage
    self.dodge_chance = dodge_chance
    self.inventory = []
    Character.all_characters.append(self)

  def __str__(self):
    return f"{self.__class__.__name__}, name: '{self.name}'"
  
  def __gt__(self, opponent):
    return self.damage > opponent.damage

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
    print(f"{self.__class__.__name__} '{self.name}':")
    print(f"HP: {self.hp}")
    print(f"DMG: {self.damage}")
    print(f"Dodge chance: {self.dodge_chance}%")

  def add_item(self, item):
    self.inventory.append(item)

  def apply_item_effect(self):
    for item in self.inventory:
      if item.bonus_hp:
        self.hp += item.bonus_hp
      elif item.bonus_damage:
        self.damage += item.bonus_damage

  @classmethod
  def count_all_characters(cls):
    return f"Number of characters: {len(cls.all_characters)}"
  
  @classmethod
  def show_characters_stats(cls):
    for character in cls.all_characters:
      print("")
      character.show_stats()

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

magic_ketchup = Item("Magic Ketchup potion", bonus_hp = 30)
iron_sworden = Item("Iron Sworden", bonus_damage = 10)
water_fireball = Item("Water fireball", bonus_damage = 10)

print("Welcome to Brightest Sanctuary!")
while True:
  menu = input("[1] Start game\n[2] Statistics of all characters\n[3] Number of characters\n")
  if menu not in '123':
    print("Wrong number typed. Choose again")
    continue
  match menu:
    case '1':
      break
    case '2':
      Character.show_characters_stats()
    case '3':
      print(Character.count_all_characters())

while True:
  choose_character = input("Choose you character:\n[1] Warrior\n[2] Rogue\n[3] Mage\n[4] Knight\n[5] Gunman\n")
  if choose_character not in '12345':
    print("Wrong number typed. Choose again.")
    continue
  match choose_character:
    case '1':
      player = warrior
      break
    case '2':
      player = rogue
      break
    case '3':
      player = mage
      break
    case '4':
      player = knight
      break
    case '5':
      player = gunman
      break

while True:
  choose_item = input(f"Choose item:\n[1] {magic_ketchup}\n[2] {iron_sworden}\n[3] {water_fireball}\n")
  if choose_item not in '123':
    print("Wrong number typed. Choose again.")
    continue
  match choose_item:
    case '1':
      player.add_item(magic_ketchup)
      player.apply_item_effect()
      print(f"{magic_ketchup} choosen")
      break
    case '2':
      player.add_item(iron_sworden)
      player.apply_item_effect()
      print(f"{iron_sworden} choosen")
      break
    case '3':
      player.add_item(water_fireball)
      player.apply_item_effect()
      print(f"{water_fireball} choosen")
      break

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

print(f"{player} VS. {enemy}")

counter = 0
while player.hp > 0 and enemy.hp > 0:
  counter += 1
  print(f"ROUND {counter}")
  time.sleep(2)
  print("--------------------")
  print("START!")
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