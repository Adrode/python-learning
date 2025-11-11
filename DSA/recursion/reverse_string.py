text = str(input("Type a word: "))

def reverse_string(s):
  if len(s) <= 1:
    return s
  else:
    return s[-1] + reverse_string(s[:-1])
  
print(reverse_string(text))