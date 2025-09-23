# 1. Program, który sprawdza czy podana liczba jest parzysta czy nieparzysta

a = input("Type number: ")

if int(a) % 2 != 0:
  print("Number is odd")
else:
  print("Number is even")