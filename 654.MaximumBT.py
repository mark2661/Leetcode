# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums):
        self.nums = nums
        # val = max(nums)
        # idx = nums.index(val)
        return self.DFS(0, len(nums) - 1)

    def DFS(self, start, end):
        if start > end:
            return

        val = max(self.nums[start:end+1])
        idx = self.nums.index(val)
        root = TreeNode(val)
        root.left = self.DFS(start, idx-1)
        root.right = self.DFS(idx+1, end)
        return root
