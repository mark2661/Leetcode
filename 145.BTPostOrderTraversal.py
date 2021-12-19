# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        stack1 = [root]
        stack2 = []
        result = []

        while stack1:
            n = stack1.pop()
            stack2.append(n)
            if n.left:
                stack1.append(n.left)
            if n.right:
                stack1.append(n.right)

        while stack2:
            result.append(stack2.pop().val)
        return result
