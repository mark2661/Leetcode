# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isLeaf(root):
    if root:
        return root.left is None and root.right is None
    return False
def hasTwoLeaves(root):
    return isLeaf(root.left) and isLeaf(root.right)
class Solution:
    def flatten(self, root):
        if root is None or isLeaf(root):
            return root
        # if root.right:
        #     self.iot(root.right)
        # if root.left:
        #     self.iot(root.left)
        #     current = root.left
        #     while current.right:
        #         current = current.right
        #     current.right = root.right
        #     root.right = root.left
        #     root.left = None
        self.iot(root)




    def iot(self,root):
        if root is None:
            return
        # if hasTwoLeaves(root):
        #     current = root.left
        #     while current and current.right:
        #         current = current.right
        #     current.right = root.right
        #     root.right = root.left
        #     root.left = None
        #     return
        self.iot(root.left)
        self.iot(root.right)
        if root.left:
            current = root.left
            while current and current.right:
                current = current.right
            current.right = root.right
            root.right = root.left
            root.left = None
            return
