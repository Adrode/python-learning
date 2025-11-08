def is_palindrome(l):
  if len(l) <= 1:
    return True
  elif l[0] != l[-1]:
    return False
  else:
    return is_palindrome(l[1:-1])

print(is_palindrome([1, 2, 5, 4, 1]))