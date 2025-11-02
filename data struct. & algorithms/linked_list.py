class SinglyNode:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    return str(self.value)
  
Head = SinglyNode(1)
A = SinglyNode(4)
B = SinglyNode(9)
C = SinglyNode(11)
D = SinglyNode(32)

Head.next = A
A.next = B
B.next = C
C.next = D

def display(head):
  current = head
  elements = []
  while current:
    elements.append(str(current.value))
    current = current.next
  return ' -> '.join(elements)

print(display(Head))

def search(head, value):
  current = head
  position = 1
  while current:
    if current.value == value:
      return f"{value} at position {position}"
    current = current.next
    position += 1

print(search(Head, 11))