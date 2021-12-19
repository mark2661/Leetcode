# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_paths(root,result,currentPath):
    if root == None:
        return

    currentPath += "->{}".format(str(root.val)) if len(currentPath) > 0 else str(root.val)
    if isLeaf(root):
        result.append(currentPath)
        return

    tree_paths(root.left,result,currentPath)
    tree_paths(root.right, result, currentPath)

def isLeaf(root):
    return root.left == None and root.right == None

class Solution:
    def binaryTreePaths(self, root):
        result = []
        tree_paths(root,result,"")
        return result
