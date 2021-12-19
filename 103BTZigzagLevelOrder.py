# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        q = deque()
        q.append(root)
        result = []
        flip = False
        while len(q) > 0:
            level = []
            next_level = []
            while len(q) > 0:
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if flip:
                result.append(level[-1::-1])
            else:
                result.append(level)

            for i in range(len(next_level)):
                q.append(next_level[i])

            flip = not flip

        return result

root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
my_solution = Solution()
my_solution.zigzagLevelOrder(root)