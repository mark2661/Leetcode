# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_tree(root):
    if root == None:
        return 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)

def tilt(root):
    if root == None:
        return 0
    t = abs(sum_tree(root.left) - sum_tree(root.right))
    return t + tilt(root.left) + tilt(root.right)


class Solution:
    def findTilt(self, root):
        return tilt(root)


