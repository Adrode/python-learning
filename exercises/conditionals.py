calculation_type = input("1. Dodawanie, 2. Odejmowanie, 3. Mnożenie, 4. Dzielenie: ")
a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę: ")
a = int(a)
b = int(b)

match calculation_type:
  case '1':
    print(a + b)
  case '2':
    print(a - b)
  case '3':
    print(a * b)
  case '4':
    print(a / b)
  case _:
    print("Wybrano niewłaściwą opcję")