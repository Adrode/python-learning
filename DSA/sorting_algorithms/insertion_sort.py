# Insertion sort
#   Time O(n^2)
#   Space O(1)

A = [-10, 1, 15, 3, 2, 5, 6, -1, 3]

def insertion_sort(arr):
  n = len(arr)
  for i in range(1, n):
    print(f"{i}: ")
    for j in range(i, 0, -1):
      if arr[j] < arr[j-1]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        print(f"{i}.{j}: {arr}")
      else:
        break

insertion_sort(A)
print(A)