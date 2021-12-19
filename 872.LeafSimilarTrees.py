
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafValueSequence(root):
    if root is None:
        return []
    if isLeaf(root):
        return [root.val]
    return [] + leafValueSequence(root.left) + leafValueSequence(root.right)

def isLeaf(root):
    return root.left is None and root.right is None

class Solution:
    def leafSimilar(self, root1, root2):
        lvs1 = leafValueSequence(root1)
        lvs2 = leafValueSequence(root2)

        if len(lvs1) != len(lvs2):
            return False
        for i in range(len(lvs1)):
            if lvs1[i] != lvs2[i]:
                return False
        return True