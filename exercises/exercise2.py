# 2. Program, który sprawdza czy liczba jest <, > czy == 0

a = int(input("Type number: "))

if a > 0:
  print(f"{a} > 0")
elif a < 0:
  print(f"{a} < 0")
elif a == 0:
  print(f"{a} == 0")
else:
  print("Something went wrong")