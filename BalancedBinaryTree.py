# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left),height(root.right))

def balanced(root):
    if root == None:
        return True

    return abs(height(root.left) - height(root.right)) <= 1 and balanced(root.left) and balanced(root.right)

class Solution:
    def isBalanced(self, root):
        return balanced(root)
