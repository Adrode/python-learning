class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.val)

#         1
#       /   \
#     2       3
#    / \     /
#   4   5   10

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

nodes = [A, B, C, D, E, F]

# DFS:
def pre_order(node):
  if not node:
    return
  
  print(node)
  pre_order(node.left)
  pre_order(node.right)
  
print("Pre order traversal: ")
pre_order(A)

def pre_order_iterative(node):
  elements = []
  stack = [node]

  while stack:
    current = stack.pop()
    if current:
      elements.append(current.val)
      stack.append(current.right)
      stack.append(current.left)
  return elements

print("Pre order iterative traversal: ")
print(pre_order_iterative(A))

def in_order(node):
  if not node:
    return
  
  in_order(node.left)
  print(node)
  in_order(node.right)
  
print("In order traversal: ")
in_order(A)

def post_order(node):
  if not node:
    return
  
  post_order(node.left)
  post_order(node.right)
  print(node)
  
print("Post order traversal: ")
post_order(A)

# BFS:
from collections import deque

def level_order(node):
  q = deque()
  q.append(node)

  while q:
    node = q.popleft()
    print(node)
    if node.left: q.append(node.left)
    if node.right: q.append(node.right)

print("BFS:")
level_order(A)

# Search in binary tree - DFS:
def dfs_search(node, search):
  if not node:
    return False
  
  if node.val == search:
    return True
  
  return dfs_search(node.left, search) or dfs_search(node.right, search)

print(dfs_search(A, 9))