# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isLeaf(root):
    return root.left == None and root.right == None

def path_sum(root,total,target):
    if root == None:
        return False
    if isLeaf(root):
        return root.val + total == target

    total += root.val
    return path_sum(root.left, total, target) or path_sum(root.right, total, target)

class Solution:
    def hasPathSum(self, root, targetSum):
        return path_sum(root, 0, targetSum)