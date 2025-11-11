import heapq

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

heapq.heapify(A)
print(A)

heapq.heappush(A, 4)
print(A)

heapq.heappop(A)
print(A)

B = [15, -5, 2, 4, 1, -1, 11, 6, 4]

def heapsort(arr):
  heapq.heapify(arr)
  n = len(arr)
  new_list = [0] *  n

  for i in range(n):
    minn = heapq.heappop(arr)
    new_list[i] = minn

  return new_list

print(f"Heapsort: {B} -> {heapsort(B)}")

heapq.heappushpop(A, 99)
print(A)