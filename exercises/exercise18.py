# 18. Program, który wskazuje najczęściej pojawiający się string w list (pomija wielkość liter)

sentences = [
  "Ala ma kota.",
  "Kot ma Ale!",
  "Czy Ala kocha kota?",
  "Kot to najlepszy przyjaciel Ali."
]

most_common_string = {}

for element in sentences:
  for item in element.split(" "):
    item = item.lower()

    if item[-1] in ".,?!":
        item = item[0:-1]

    if not item in most_common_string:
      most_common_string[item] = 1
    else:
      value = most_common_string.get(item) + 1
      most_common_string[item] = value

print(max(most_common_string, key=most_common_string.get))

  
      