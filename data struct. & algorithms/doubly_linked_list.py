class Node:
  def __init__(self, value, next=None, prev=None):
    self.value = value
    self.next = next
    self.prev = prev

  def __str__(self):
    return str(self.value)
  
class DoublyLinkedList:
  def __init__(self, head=None, tail=None):
    self.head = head
    self.tail = tail

  def append(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node

  def prepend(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = self.tail = new_node
    else:
      self.head.prev = new_node
      new_node.next = self.head
      self.head = new_node

  def display_forward(self):
    current = self.head
    elements = []
    while current:
      elements.append(str(current.value))
      current = current.next
    print(f"Forwards: {' <-> '.join(elements)}")

  def display_backward(self):
    current = self.tail
    elements = []
    while current:
      elements.append(str(current.value))
      current = current.prev
    print(f"Backwards: {' <-> '.join(elements)}")

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.prepend(3)
dll.append(9)
dll.append(11)
dll.prepend(5)

dll.display_forward()
dll.display_backward()