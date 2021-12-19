# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isLeaf(root):
    return root.left is None and root.right is None


class Solution:
    def pathSum(self, root, targetSum):
        self.result = []
        self.root = root
        self.targetSum = targetSum
        self.pathSumRecursive(self.root, self.targetSum, [])
        return self.result

    def pathSumRecursive(self,root, targetSum, path):
        if root is None:
            return

        if isLeaf(root):
            if targetSum - root.val == 0:
                path = path + [root.val]
                self.result.append(path)
                return
            else:
                return

        path = path + [root.val]

        if root.left:
            self.pathSumRecursive(root.left, targetSum - root.val, path)
        if root.right:
            self.pathSumRecursive(root.right, targetSum - root.val, path)
