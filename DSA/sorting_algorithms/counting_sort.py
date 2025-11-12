# Counting sort
#   Time
#   Space

A = [9, 4, 3, 2, 2, 9, 1, 8, 8, 7, 8, 6, 4, 5]

# temp_arr [0, 1, 2, 1, 2, 1, 1, 1, 3, 2]
#       id  0, 1, 2, 3, 4, 5, 6, 7, 8, 9

def counting_sort(arr):
  n = len(arr)
  max_value = max(arr)
  temp_arr = [0] * (max_value + 1)

  for i in range(n):
    temp_arr[arr[i]] += 1

  i = 0
  for c in range(max_value + 1):
    while temp_arr[c] > 0:
      arr[i] = c
      i += 1
      temp_arr[c] -= 1

  return arr


print(counting_sort(A))