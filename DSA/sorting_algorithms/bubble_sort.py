# Bubble Sort
#   Time O(n^2)
#   Space O(1)

A = [9, 1, 15, 3, 2, 5, 6, -1, 3]

def bubble_sort(arr):
  n = len(arr)
  check = True
  while check:
    check = False
    for i in range(1, n):
      if arr[i] < arr[i-1]:
        check = True
        arr[i-1], arr[i] = arr[i], arr[i-1]

bubble_sort(A)
print(A)