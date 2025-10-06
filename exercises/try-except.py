try:
  number = int(input("Podaj liczbę: "))
  result = 100 / number
except ValueError:
  print("Podano błędną wartość")
except ZeroDivisionError:
  print("Nie dziel przez 0, głąbie!")
else:
  print(f"Wynik 100 / {number} = {result}")
finally:
  print("I'm done...")