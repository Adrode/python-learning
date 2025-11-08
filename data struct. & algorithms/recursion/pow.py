def recursive_pow(base, exp):
  if exp == 0:
    return 1
  elif exp == 1:
    return base
  else:
    return base * recursive_pow(base, exp - 1)
  
print(recursive_pow(3, 3))