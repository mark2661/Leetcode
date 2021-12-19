# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def inorderTraversal(self, root):
#         if not root:
#             return []
#         self.result = []
#         self.stack = []
#         n= root
#         while True:
#             while n:
#                 self.stack.append(n)
#                 n = n.left
#             if len(self.stack) == 0:
#                 break
#             n = self.stack.pop()
#             self.result.append(n.val)
#             n = n.right
#
#         return self.result
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        self.seen = set()
        self.result = []
        self.stack = [root]
        while len(self.stack) > 0:
            n = self.stack.pop()
            if n in self.seen:
                self.result.append(n.val)
                continue
            if n.right:
                self.stack.append(n.right)
            self.seen.add(n)
            self.stack.append(n)
            if n.left:
                self.stack.append(n.left)

        return self.result
