# Definition for a binary tree node.
def isLeaf(root):
    return root.left is None and root.right is None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root):
        self.sum = 0
        self.DFS(root, 0)
        return self.sum

    def DFS(self, root, path):
        if root is None:
            return
        if isLeaf(root):
            path = path*10 + root.val
            self.sum += path

        path = path*10 + root.val
        self.DFS(root.left, path)
        self.DFS(root.right, path)
