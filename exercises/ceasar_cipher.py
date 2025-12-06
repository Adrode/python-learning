def ceasar(text, key):
  text = text.lower()
  result = ""
  for char in text:
    code = ord(char)
    shift = code + key
    if shift > 122:
      code = (shift - 122) + 96
    else:
      code = shift
    result += chr(code)

  return result

print(ceasar("xyz", 1))