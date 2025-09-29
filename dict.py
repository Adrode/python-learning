phone_book = {
  "Hanna": 8,
  "Adrian": 555444333,
  "Inna": 222777999,
  "Hanna": 10
}

# print(phone_book)
# print(phone_book.get("Kuba"))
# print(phone_book["Adrian"])
# # print(phone_book["Kuba"]) // KeyError

# phone_book["Kuba"] = 432543654
# phone_book["Adrian"] = 1
# phone_book.pop("Hanna")
# print(phone_book)

for element in phone_book: # keys
  print(element)

for element in phone_book.values(): # values
  print(element)

for element in phone_book.items(): # keys and values
  print(element)

for element in phone_book.items():
  print(f"{element[0]}: {element[1]}")

for name, number in phone_book.items():
  print(f"{name}: {number}")