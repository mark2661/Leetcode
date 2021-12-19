# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root):
        if root is None:
            return 0
        self.level = 0
        self.q = [root]
        self.BFS()
        return pow(2,self.level) - 1 + len(self.q)

    def BFS(self):
        while len(self.q) == pow(2,self.level):
            new_level = []
            for n in self.q:
                if n.left:
                    new_level.append(n.left)
                if n.right:
                    new_level.append(n.right)
            self.q = new_level
            self.level += 1
