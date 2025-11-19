import re

text = input("Type text: ")

# email
email_pattern = r"[a-zA-Z0-9.-_]+@[a-zA-Z]+\.(com|net|org|edu)"

if re.search(email_pattern, text):
  print("There is a valid email")
else:
  print("There is no email")

# only digits
only_digits = r"\b[0-9]+\b"

if re.search(only_digits, text):
  print("There is an only-digits")
else:
  print("There is no only-digits")

# fullname
full_name = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
if re.search(full_name, text):
  print("There is a fullname")
else:
  print("There is no fullname")