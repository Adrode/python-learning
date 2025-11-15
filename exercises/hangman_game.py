import random

stages = {
    0: "",
    1: "|",
    2: """|
|""",
    3: """|
|
|""",
    4: """|
|
|
|""",
    5: """____
|
|
|
|""",
    6: """____
|  |
|
|
|""",
    7: """____
|  |
|  o
|
|""",
    8: """____
|  |
|  o
| /
|""",
    9: """____
|  |
|  o
| /|
|""",
    10: """____
|  |
|  o
| /|\\
|""",
    11: """____
|  |
|  o
| /|\\
| /""",
    12: """____
|  |
|  o
| /|\\
| / \\""" }

words = ['pineapple', 'banana', 'Nagasaki', 'ludology', 'bambino', 'ratatouille']
i = 0

def draw_a_word(arr):
  word = random.choice(arr)
  return word.lower()

def print_hangman(dict, counter):
  print(dict[counter])

def type_word(counter):
  word = draw_a_word(words)
  blanks = ['_'] * len(word)
  seen = set()

  while counter < 12:
    draw = str(input("Type one character: ")).lower()
    if len(draw) != 1:
      print("Too many characters typed!")
      continue
    elif draw in seen:
      print("This character was typed earlier. Type another one.")
      continue

    seen.add(draw)
    print(f"Typed characters: {seen}")
    
    if draw in word:
      for index, char in enumerate(word):
        if draw == char:
          blanks[index] = draw
    else:
      counter += 1

    print_hangman(stages, counter)
    print(' '.join(blanks))
    
    if '_' not in blanks:
      return "You won!"
    
  return f"You lost! The word was: {word}"

print("HANGMAN - Guess a word")
print(type_word(i))