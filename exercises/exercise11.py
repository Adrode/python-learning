# 11. Program, który pobiera od użytkownika 3 liczby całkowite i wyświetla je w kolejności od najmniejszej do największej

a = input("Podaj liczbę a: ")
b = input("Podaj liczbę b: ")
c = input("Podaj liczbę c: ")

if a < b and a < c:
  if b < c:
    print(f"1. a:  {a} ,b:  {b} ,c:  {c}")
  else:
    print(f"2. a:  {a} ,c:  {c} ,b:  {b}")
elif b < a and b < c:
  if a < c:
    print(f"3. b:  {b} ,a:  {a} ,c:  {c}")
  else:
    print(f"4. b:  {b} ,c:  {c} ,a:  {a}")
else:
  if a < b:
    print(f"5. c:  {c} ,a:  {a} ,b:  {b}")
  else:
    print(f"6. c: , {c}, ,b:  {b} ,a:  {a}")