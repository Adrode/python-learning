counter = 0

def increment_counter():
  global counter
  for i in range(0, 3):
    counter += 1

increment_counter()
print(counter)