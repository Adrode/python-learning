def nested_list_sum(l):
  if len(l) == 0:
    return 0
  elif len(l) == 1:
    return nested_list_sum(l[0]) if isinstance(l[0], list) else l[0]
  else:
    last = nested_list_sum(l[-1]) if isinstance(l[-1], list) else l[-1]
    return last + nested_list_sum(l[:-1])
    
print(nested_list_sum([1, [2, 3], [4, [5, 6]], 7]))