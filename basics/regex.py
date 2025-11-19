import re

text = input("Type text: ")

# email
email_pattern = r"^[a-zA-Z0-9.-_]+@[a-zA-Z]+\.(com|net|org|edu)$"

if re.search(email_pattern, text):
  print("It's a valid email")

# only digits
only_digits = r"^[0-9]+$"

if re.search(only_digits, text):
  print("It's an only-digits")

# fullname
full_name = r"^[A-Z][a-z]+ [A-Z][a-z]+$"
if re.search(full_name, text):
  print("It's a fullname")