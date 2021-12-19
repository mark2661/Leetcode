# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        self.ht = dict()
        self.pidx = 0
        self.preorder = preorder

        for i in range(len(inorder)):
            self.ht[inorder[i]] = i

        return self.ArrayToBST(0,len(inorder)-1)

    def ArrayToBST(self,start,end):
        if start > end:
            return None
        root = TreeNode(self.preorder[self.pidx])
        root_idx = self.ht[self.preorder[self.pidx]]
        self.pidx += 1
        root.left = self.ArrayToBST(start, root_idx - 1)
        root.right = self.ArrayToBST(root_idx + 1, end)
        return root
