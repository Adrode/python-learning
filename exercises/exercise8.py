# 8. Funkcja, która sprawdza czy podany string jest palindromem (czyta się go tak samo od przodu, jak i od tyłu)

word = input("Podaj słowo: ")

# def is_palindrome(word):
#   reverse = list(word)
#   reverse.reverse()
#   reverse = "".join(reverse)

#   if word == reverse:
#     print(f"Is {word} a palindrome?: {True}")
#   else:
#     print(f"Is {word} a palindrome?: {False}")

# is_palindrome(word)

def is_palindrome2(word):
  for i in range(0, len(word) // 2):
    if word[i] != word[-(i + 1)]:
      print(f"{False}, {word} is not a palindrome")
      break
  else:
    print(f"{True}, {word} is a palindrome")

is_palindrome2(word)