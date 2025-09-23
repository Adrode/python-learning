text = "abcdefghij"

def alt_endswith(string, search):
  string_len = len(string)
  search_len = len(search)
  last_char_of_string = string[string_len - search_len]

  if search_len <= 0:
    return print(True, "- searched string's length is 0")
  elif search_len == 1:
    if last_char_of_string == search:
       return print(True)
    else: return print(False)
  else:
    for i in range(search_len):
      if string[string.index(last_char_of_string) + i] != search[i]:
        return print(False, f"- index {i} of search string is incorrect")
    print(True)
        
alt_endswith(text, "hij")