# 5. Program, który wyświetli wszystkie liczby pierwsze od 1 do 100import math

a = 1

while a < 100:
  a += 1
  for i in range(2, a):
    if a % i == 0:
      break
  else:
    print(a)