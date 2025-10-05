import time

i = 1

while i < 10:
  print(i)
  i += 1
  time.sleep(1)
# ------------------------

for i in range(0, 4):
  print(i)
for i in "JakiS_StriNGG":
  print(i)
for _ in range(0, 2):
  print("Hello world!")
# ------------------------

for i in range(0, 5):
  if i == 2:
    continue
  print(i)
# ------------------------

for i in range(0, 5):
  if i == 2:
    break
  print(i)