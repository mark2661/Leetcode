
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def isLeaf(root):
    return root.left is None and root.right is None

# class Solution:
#     def connect(self, root):
#         if not root:
#             return root
#         self.DFS(root)
#         return root
#
#     def DFS(self, root):
#         if root is None or isLeaf(root):
#             return
#         if root.left:
#             if root.right:
#                 root.left.next = root.right
#             else:
#                 current = root
#                 while current.next:
#                     current = current.next
#                     if current.left:
#                         root.left.next = current.left
#                         break
#                     elif current.right:
#                         root.left.next = current.right
#                         break
#         if root.next and root.right:
#             if root.next.left:
#                 root.right.next = root.next.left
#             else:
#                 current = root
#                 while current.next:
#                     current = current.next
#                     if current.left:
#                         root.right.next = current.left
#                         break
#                     elif current.right:
#                         root.right.next = current.right
#                         break
#         self.DFS(root.right)
#         self.DFS(root.left)

class Solution:
    def connect(self, root):
        if not root:
            return root
        self.DFS(root)
        return root

    def DFS(self, root):
        if root is None or isLeaf(root):
            return
        c = root.next
        scanner = None
        while c:
            if c.left:
                scanner = c.left
                break
            elif c.right:
                scanner = c.right
                break
            c = c.next
        if root.right:
            root.right.next = scanner
        if root.left:
            root.left.next = root.right if root.right else scanner
        self.DFS(root.right)
        self.DFS(root.left)



