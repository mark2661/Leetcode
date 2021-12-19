# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        if root is None:
            return root
        self.DFS(root)
        return root

    def DFS(self, root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.DFS(root.left)
        self.DFS(root.right)
        return
