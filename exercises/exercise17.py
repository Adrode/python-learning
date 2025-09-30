# 17. Program, który przyjmuje od użytkownika tekst z konsoli, a następnie
# tworzy słownik, w którym kluczami są słowa wpisane przez
# użytkownika, a wartościami liczby wystąpień danego słowa w tekście

text = input("Podaj tekst składający się z wielu słów: ")
dict = {}

for item in text.split(" "):
  if dict.get(item, 0) == 0:
    dict.update({item: 1})
  elif not dict.get(item, 0) == 0:
    value = dict.get(item) + 1
    dict.update({item: value})

print(dict)