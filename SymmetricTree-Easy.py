
#Recurrsive solution
def symmetric(left_sub,right_sub):

    if left_sub == None and right_sub == None:
        return True
    elif left_sub != None and right_sub != None:
        return left_sub.val == right_sub.val and symmetric(left_sub.left,right_sub.right) and symmetric(left_sub.right,right_sub.left)
    return False

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        return True if root is None else symmetric(root.left, root.right)