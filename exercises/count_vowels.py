def count_vowels(word):
  word = word.lower()
  vowels = "aeuio"
  return sum(1 for char in word if char in vowels)

print(count_vowels("ananasowy"))