# Hashsets

s = set()

# Operacje na O(1)
s.add(1) # O(1)
s.add(5)
print(s)
s.remove(1) # O(1)
print(s)
s.add(10)
s.add(20)
print(11 in s) # O(1)

# Set contstructor - O(s), gdzie s to liczba elementów stringa
text = 'aaaaabbbbbbbcccccccccddddddeeeeeeeeeeee'
text_set = set(text)
print(text_set)

# Pętla na set O(n), bo pętla z założenia musi przechodzić po elementach
for item in text_set:
    print(item)

print('------------')
# Hashmaps - czyli Dictionaries

d = {
    'greg': 5,
    'adrian': 8,
    'daniel': 15
    }

# Operacje na O(1)
print(d['adrian']) # O(1), odczytanie value dla wskazanego key

d['jacob'] = 5 # O(1), dodanie elementu
print(d)

del d['greg'] # O(1), usunięcie elementu
print(d)

print('adrian' in d) # O(1), wyszukanie elementu

for key, value in d.items(): # O(n), bo to pętla
    print(f"{key}: {value}")

print('------------')
# defaultdict
from collections import defaultdict

default = defaultdict(list)
default['kekw'] = 1
default['3'] = 5
default[2]
print(default)