import random

rand_number = random.randrange(1,1000)
a = None
i = 0

print("Find a number from 1 to 1000!")

while a != rand_number:
  i += 1
  a = input("Type number: ")
  a = int(a)
  if a > rand_number:
    print("Too much")
  elif a < rand_number:
    print("Too low")
  elif a == rand_number:
    print(f"You won! Winning number is {rand_number}. Steps: {i}")
    