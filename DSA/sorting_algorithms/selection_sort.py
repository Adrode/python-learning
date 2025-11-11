# Selection sort
#   Time
#   Space

A = [9, -10, 1, 15, 3, 2, 5, 6, -1, 3]

def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_element = i
    for j in range(i+1, n):
      if arr[j] < arr[min_element]:
        min_element = j
    arr[i], arr[min_element] = arr[min_element], arr[i]

selection_sort(A)
print(A)