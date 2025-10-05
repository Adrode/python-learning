# 19. Program, który za pomocą funkcji wyświetla wartości dla podanego klucza

import time

countries = {
  "Polska": ("Warszawa", 38),
  "Niemcy": ("Berlin", 83),
  "Francja": ("Paryż", 57)
}

def country_info(name):
  print(f"Stolica: {countries[str(name)][0]}, liczba mieszkańców (mln): {countries[str(name)][1]}")

def country_add(name, capital, population):
  countries[str(name)] = (str(capital), int(population))

while True:
  time.sleep(1)
  menu = input("-------------------------------\nKRAJE - Stolice i liczba ludności\n[1] Sprawdź informacje o kraju\n[2] Dodaj informacje o kraju\n[0] Wyjście\n")

  if menu in "0":
    break
  elif menu not in "12":
    print("Wybrano niewłaściwą opcję z menu")
    continue
  
  country = input("Podaj nazwę kraju: ")

  if menu == "1":
    if country in countries:
         country_info(country)
    else:
      print("Brak wpisu na temat tego kraju")
  elif menu == "2":
    if country in countries:
      print("Wpis o tym kraju już istnieje")
    else:
      capital = input("Podaj stolicę kraju: ")
      population = input("Podaj liczbę mieszkańców kraju [mln]: ")
      country_add(country, capital, population)
  elif menu == "0":
    break