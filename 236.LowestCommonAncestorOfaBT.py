# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        self.ht = {root.val:None}
        self.foundP = False
        self.foundQ = False
        self.p = p
        self.q = q
        self.DFS(root)
        pLst = self.makeLst(p)
        pLst.add(p)
        if q in pLst:
            return q
        while q not in pLst:
            q = self.ht[q.val]
        return q



    def DFS(self, root):
        if root is None or (self.foundQ and self.foundP):
            return
        if root == self.q:
            self.foundQ = True
        elif root == self.p:
            self.foundP = True

        if root.left:
            self.ht[root.left.val] = root
        if root.right:
            self.ht[root.right.val] = root

        self.DFS(root.left)
        self.DFS(root.right)

    def makeLst(self, node):
        current = node
        s= set()
        while current:
            s.add(self.ht[current.val])
            current = self.ht[current.val]
        return s



# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x, left = None, right = None):
#         self.val = x
#         self.left = left
#         self.right = right
#
# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         self.foundP = False
#         self.foundQ = False
#         self.pPath = None
#         self.qPath = None
#         self.p = p
#         self.q = q
#         self.DFS(root,[])
#
#         if len(self.pPath) < len(self.qPath):
#             if p in self.qPath:
#                 return p
#             else:
#                 pPointer = 0
#                 qPointer = len(self.qPath) - len(self.pPath)
#                 while pPointer < len(self.pPath) and qPointer < len(self.qPath):
#                     if self.pPath[pPointer] == self.qPath[qPointer]:
#                         return self.pPath[pPointer]
#                     pPointer += 1
#                     qPointer += 1
#         if len(self.qPath) < len(self.pPath):
#             if q in self.pPath:
#                 return q
#             else:
#                 pPointer = len(self.pPath) - len(self.qPath)
#                 qPointer = 0
#                 while pPointer < len(self.pPath) and qPointer < len(self.qPath):
#                     if self.pPath[pPointer] == self.qPath[qPointer]:
#                         return self.pPath[pPointer]
#                     pPointer += 1
#                     qPointer += 1
#
#         pointer = 0
#         while pointer < len(self.pPath) and pointer < len(self.qPath):
#             if self.pPath[pointer] == self.qPath[pointer]:
#                 return self.pPath[pointer]
#             pointer += 1
#
#
#
#     def DFS(self, root,path):
#         if (self.foundP and self.foundQ) or root is None:
#             return
#         if root == self.p:
#             self.foundP = True
#             self.pPath = path
#         elif root == self.q:
#             self.foundQ = True
#             self.qPath = path
#
#         self.DFS(root.left, [root] + path)
#         self.DFS(root.right, [root] + path)


eightRoot = TreeNode(8)
nTwoRoot = TreeNode(-2,eightRoot)
fourRoot = TreeNode(4)
zeroRoot = TreeNode(0,nTwoRoot,fourRoot)
threeRoot = TreeNode(3)
nOneRoot = TreeNode(-1,zeroRoot,threeRoot)
my_solution = Solution()
print(my_solution.lowestCommonAncestor(nOneRoot, eightRoot,fourRoot).val)

