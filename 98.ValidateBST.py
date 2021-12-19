import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def isBST(root):
#     if root is None:
#         return True
#     if isLeaf(root):
#         return True
#
#     return root.val > getLargest(root.left) and root.val < getSmallest(root.right) and isBST(root.left) and isBST(root.right)
#
# def isLeaf(root):
#     return root.left is None and root.right is None
#
# def getSmallest(root, memo = dict()):
#     if root is None:
#         return sys.maxsize
#
#     if root in memo.keys():
#         return memo[root]
#
#     memo[root] = min(root.val, getSmallest(root.left,memo), getSmallest(root.right,memo))
#     return memo[root]
#
# def getLargest(root, memo = dict()):
#     if root is None:
#         return (-1 * sys.maxsize) - 1
#     if root in memo.keys():
#         return memo[root]
#
#     memo[root] = max(root.val, getLargest(root.left,memo), getLargest(root.right,memo))
#     return memo[root]

def isBST(root, min = (-1 * sys.maxsize) + 1, max = sys.maxsize, seen = dict()):
    if root is None:
        return True
    if root.val in seen.keys():
        return False
    if isLeaf(root):
        return True

    seen[root.val] = True
    return min < root.val < max and isBST(root.left,min,root.val,seen) and isBST(root.right,root.val, max,seen)

def isLeaf(root):
    return root.left is None and root.right is None

class Solution:
    def isValidBST(self, root):
        return isBST(root)
