# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isLeaf(root):
    return root.left is None and root.right is None
class Solution:
    def findBottomLeftValue(self, root):
        self.heights = dict()

        if isLeaf(root):
            return root.val

        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)

        if lh >= rh:
            return self.findBottomLeftValue(root.left)
        else:
            return self.findBottomLeftValue(root.right)

    def getHeight(self, root):
        if not root:
            return -1
        if root in self.heights:
            return self.heights[root]
        self.heights[root] = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        return self.heights[root]

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# def isLeaf(root):
#     return root.left is None and root.right is None
# class Solution:
#     def findBottomLeftValue(self, root):
#         self.q = [root]
#         return self.BFS()
#
#     def BFS(self):
#         while len(self.q) > 0:
#             new_level = []
#             for n in self.q:
#                 if n.left:
#                     new_level.append(n.left)
#                 if n.right:
#                     new_level.append(n.right)
#             if len(new_level) > 0:
#                 self.q = new_level
#             else:
#                 return self.q.pop(0).val