
# # Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next
#
#
#
# class Solution:
#     def connect(self, root):
#         if not root:
#             return root
#         self.q = [root]
#         self.root = root
#         self.BFS()
#         return self.root
#
#     def BFS(self):
#         while self.q:
#             new_level = []
#             for i in range(len(self.q)):
#                 if i != len(self.q) - 1:
#                     self.q[i].next = self.q[i+1]
#                 else:
#                     self.q[i].next = None
#                 if self.q[i].left:
#                     new_level.append(self.q[i].left)
#                 if self.q[i].right:
#                     new_level.append(self.q[i].right)
#             self.q = new_level

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def isLeaf(root):
    return root.left is None and root.right is None

class Solution:
    def connect(self, root):
        if not root:
            return root
        self.DFS(root)
        return root


    def DFS(self, root):
        if root is None or isLeaf(root):
            return
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left

        self.DFS(root.left)
        self.DFS(root.right)