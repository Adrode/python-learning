# with open("text.txt", "w") as f:
#   f.write("kekw")

# with open("text.txt", "a") as f:
#   f.write("\nwkek")

# with open("text.txt", "r") as f:
#   zawartosc = f.read()
#   print(zawartosc)

with open("./exercises/with_files/dane.txt", "w") as f:
  f.write("Adrian\n25\nGdańsk")

with open("./exercises/with_files/dane.txt", "r") as f:
  zawartosc = f.read()
  print(zawartosc)