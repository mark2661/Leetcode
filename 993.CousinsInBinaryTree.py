from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isCousin(root,x,y):
  q = deque()
  q.append(root)
  x_present = False
  y_present = False
  x_parent_val = -1
  y_parent_val = -1
  levelList = []

  while len(q) > 0:
      while len(q)>0:
          levelList.append(q.pop())

      for node in levelList:
          if hasLeftChild(node):
              if node.left.val == x:
                  x_present = True
                  x_parent_val = node.val
              if node.left.val == y:
                  y_present = True
                  y_parent_val = node.val
          if hasRightChild(node):
              if node.right.val == x:
                  x_present = True
                  x_parent_val = node.val
              if node.right.val == y:
                  y_present = True
                  y_parent_val = node.val


      if x_present:
          return y_present and y_parent_val != x_parent_val and y_parent_val != -1
      if y_present:
          return x_present and y_parent_val != x_parent_val and y_parent_val != -1

      for node in levelList:
          if node.left:
              q.append(node.left)
          if node.right:
              q.append(node.right)
      levelList.clear()


def hasLeftChild(root):
    return root.left != None

def hasRightChild(root):
    return root.right != None

class Solution:
    def isCousins(self, root, x, y):
        return isCousin(root,x,y)