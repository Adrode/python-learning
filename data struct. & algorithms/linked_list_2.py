class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data)
  
class LinkedList:
  def __init__(self, head=None):
    self.head = head

  def append_node(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node

  def display(self):
    current = self.head
    elements = []
    while current:
      elements.append(str(current.data))
      current = current.next
    print(' -> '.join(elements))

linked_list = LinkedList()
linked_list.append_node(1)
linked_list.append_node(4)
linked_list.append_node(9)
linked_list.append_node(15)
linked_list.append_node(17)

linked_list.display()