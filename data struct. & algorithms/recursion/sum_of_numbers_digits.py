num = input("Type a number: ")

def sum_of_digits(n):
  if len(n) <= 1:
    return int(n)
  else:
    return int(n[-1]) + sum_of_digits(n[:-1])
  
print(sum_of_digits(num))