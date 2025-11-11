from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(9)
print(queue)

queue.pop()
print(queue)

print(queue[0])