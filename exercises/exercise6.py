# 6. Program, który wyświetli sumę wszystkich liczb parzystych z przedziału 1-100

a = 0
sum = 0

while a <= 100:
  if a % 2 == 0:
    sum += a
    print(f"{a}: {sum}")
  a += 1

print(f"Total sum: {sum}")