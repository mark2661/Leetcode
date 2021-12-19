# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findFrequentTreeSum(self, root):
        self.ht = dict()
        self.max_frequency = 0
        self.sums = []
        self.DFS(root)

        for key in self.ht.keys():
            if self.ht[key] > self.max_frequency:
                self.max_frequency = self.ht[key]
                self.sums = [key]
            elif self.ht[key] == self.max_frequency:
                self.sums.append(key)
        return self.sums

    def DFS(self, root):
        if not root:
            return 0
        sum = root.val
        if root.left:
            sum += self.DFS(root.left)
        if root.right:
            sum += self.DFS(root.right)
        if sum in self.ht:
            self.ht[sum] += 1
        else:
            self.ht[sum] = 1
        return sum
