A = [8, 14, -5, -21, -1, 4, 0, 6, 5, 2, 5, 1]

def selection_sort(arr):
  n = len(arr)

  for i in range(n):
    min_value = i
    for j in range(i+1, n):
      if arr[min_value] > arr[j]:
        min_value = j
    arr[i], arr[min_value] = arr[min_value], arr[i]

print(f"A: {A}")

selection_sort(A)
print(f"Selection sort: {A}")

B = [-25, 15, -4, -2, 11, 5, 2, -13, 4, 7, 0, 9, 1]

def insertion_sort(arr):
  n = len(arr)
  for i in range(1, n):
    for j in range (i, 0, -1):
      if arr[j] < arr[j-1]:
        arr[j], arr[j-1] = arr[j-1], arr[j]

print(f"\nB: {B}")

insertion_sort(B)
print(f"Insertion sort: {B}")

C = [12, 15, -7, 2, -11, 5, -2, -13, 4, 7, -30, 9, 1]

def bubble_sort(arr):
  n = len(arr)
  flag = True

  while flag:
    flag = False
    for i in range(1, n):
      if arr[i] < arr[i-1]:
        flag == True
        arr[i], arr[i-1] = arr[i-1], arr[i]

print(f"\nC: {C}")

bubble_sort(C)
print(f"Bubble sort: {C}")