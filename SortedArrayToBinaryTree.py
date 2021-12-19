# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_node(nums,l,r):
    if l > r:
        return None

    mid = (l + r) // 2
    new_node = TreeNode(nums[mid])
    new_node.left = create_node(nums, l , mid - 1)
    new_node.right = create_node(nums, mid + 1, r)

    return new_node
class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) > 0:
            return create_node(nums, 0, len(nums) - 1)
        else:
            return None