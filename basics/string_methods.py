book_name = "JakAs DłUGa nazwA kSIążKi  ß "
book_name2 = "JakAs DłUGa nazwA kSIążKi  ss "

print(book_name.strip())
print(book_name.upper())
print(book_name.capitalize())
print(book_name.lower())
print(book_name.casefold())

print(book_name.count("a"))

print(book_name.find("a"))
print(book_name.index("a"))
print(book_name.startswith("J")) # True
print(book_name.endswith(" ")) # True

print(book_name.replace("nazwA", "tytuł"))
print(book_name.split(" " or "a"))

print("\n\ncasefold vs lower")
print(book_name.lower() == book_name2.lower()) # False
print(book_name.casefold() == book_name2.lower()) # True
print(book_name.casefold() == book_name2.casefold()) # True
print(book_name.upper().lower() == book_name2.lower()) # True