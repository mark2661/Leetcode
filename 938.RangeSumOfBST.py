

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSum(root,low,high):
    if root is None:
        return 0

    node_val = root.val if low <= root.val <= high else 0
    if isLeaf(root):
        return node_val

    return node_val + rangeSum(root.left,low,high) + rangeSum(root.right,low,high)

def isLeaf(root):
    return root.left is None and root.right is None

class Solution:
    def rangeSumBST(self, root, low, high):
        return rangeSum(root,low,high)
