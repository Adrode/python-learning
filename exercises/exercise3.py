# 3. Program, który zapyta użytkownika o wynik na egzaminie (od 0 do 100) i wyświetli ocenę
# 90 - 100 -> 5
# 80 - 89 -> 4
# 70 - 79 -> 3
# 60 - 69 -> 2
# poniżej 60 -> 1

a = int(input("Type your score (0-100): "))

if a >= 90 and a <= 100:
  print("Your rate is: 5")
elif a >= 80 and a < 90:
  print("Your rate is: 4")
elif a >= 70 and a < 80:
  print("Your rate is: 3")
elif a >= 60 and a < 70:
  print("Your rate is: 2")
elif a < 60:
  print("Your rate is: 1")
else:
  print("Your score is out of range. Try again")