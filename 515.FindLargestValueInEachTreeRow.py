# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root):
        if not root:
            return []
        self.max_vals = []
        self.q = [root]
        self.BFS()
        return self.max_vals

    def BFS(self):
        while self.q:
            new_level = []
            m = -1 * pow(2,31)
            for n in self.q:
                m = max(m, n.val)
                if n.left:
                    new_level.append(n.left)
                if n.right:
                    new_level.append(n.right)
            self.max_vals.append(m)
            self.q = new_level

