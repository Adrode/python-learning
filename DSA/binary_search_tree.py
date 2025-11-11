class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.val)
  
A = Node(5)
B = Node(1)
C = Node(8)
D = Node(-1)
E = Node(3)
F = Node(7)
G = Node(9)

A.left, A.right = B, C
B.left, B.right = D, E
C.left, C.right = F, G

def search_bst(node, search):
  if not node:
    return False
  
  if node.val == search:
    return True
  
  if search < node.val: return search_bst(node.left, search)
  else: return search_bst(node.right, search)

print(search_bst(A, 9))