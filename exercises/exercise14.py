# 14. Program, który zwraca najmniejszą i największą liczbę z listy zawierającej 10 liczb całkowitych

numbers = [83, 19, 232, 999, 17, 54, 421, -12, 433, 10]
min = numbers[0]
max = numbers[0]

for number in numbers:
  if number <= min:
    min = number
  elif number > max:
    max = number

print(min)
print(max)