counter = int(input("Type any number: "))

def countdown(n):
  if n == 0:
    return f"Start!"
  else:
    print(n)
    return countdown(n - 1)
  
print(countdown(counter))