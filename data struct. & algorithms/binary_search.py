nums = [-9, -5, -1, 0, 2, 4, 12, 31]
#        0,  1,  2, 3, 4, 5,  6,  7
search_num = 4

def binary_search(arr, T):
  N = len(arr)
  L = 0
  R = N - 1
  M = (L + R) // 2
  print(f"L: {L}, R: {R}, M: {M}")

  while L <= R:
    M = (L + R) // 2

    if arr[M] == T:
      return True
    elif arr[M] < T:
      L = M + 1
      print(f"L: {L}, R: {R}, M: {M}")
    elif arr[M] > T:
      R = M - 1
      print(f"L: {L}, R: {R}, M: {M}")

  return False
    
print(binary_search(nums, search_num))