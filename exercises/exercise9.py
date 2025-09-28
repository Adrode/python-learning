# 9. Program, który sprawdza czy imię jest męskie czy żeńskie (zakładam, że żeńskie kończą się na 'a')

name = input("Podaj imię: ")

if name[-1] == "a":
  print("Imię żeńskie")
else:
  print("Imię męskie")