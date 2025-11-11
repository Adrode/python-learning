def is_even(n):
  if n == 0:
    return True
  if n == 1:
    return False
  else:
    return is_even(n - 2)
  
print(is_even(16))