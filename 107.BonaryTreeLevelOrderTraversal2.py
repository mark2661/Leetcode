# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []
        self.q = []
        self.result = [[root.val]]
        self.q.append(root)
        self.BFS()
        return self.result

    def BFS(self):
        while len(self.q) > 0:
            level = []
            while len(self.q) > 0:
                node = self.q.pop(0)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if len(level) > 0:
                self.result.insert(0,[n.val for n in level])
            self.q = level



my_solution = Solution()
print(my_solution.levelOrderBottom(TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(3,None,TreeNode(5)))))


