import sys

def minimumDiff(root):
    if root == None or isLeaf(root):
        return sys.maxsize
    elif root.left is None:
        currentMin = abs(root.val - findSmallest(root.right))
    elif root.right is None:
        currentMin = abs(root.val - findLargest(root.left))
    else:
        currentMin = min(abs(root.val - findLargest(root.left)), abs(root.val - findSmallest(root.right)))

    return min(currentMin,minimumDiff(root.left),minimumDiff(root.right))

def isLeaf(root):
    return root.left == None and root.right == None

def findSmallest(root):
    currentRoot = root
    while currentRoot is not None and currentRoot.left is not None:
        currentRoot = currentRoot.left
    return currentRoot.val if currentRoot is not None else sys.maxsize

def findLargest(root):
    currentRoot = root
    while currentRoot is not None and currentRoot.right is not None:
        currentRoot = currentRoot.right
    return currentRoot.val if currentRoot is not None else sys.maxsize


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root):
        return minimumDiff(root)
