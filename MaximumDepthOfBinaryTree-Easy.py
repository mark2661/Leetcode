
# Definition for a binary tree node.
def maxD(root,count):
    if root == None:
        return count
    count += 1
    return max(maxD(root.left, count), maxD(root.right, count))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        return maxD(root,0)
