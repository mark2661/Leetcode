# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isLeaf(node):
    return node.left == None and node.right == None

def isSameTreeRecursive(treeOneNode,treeTwoNode):
    if treeOneNode and treeTwoNode:
        return True

    if (treeOneNode and not treeTwoNode) or (treeTwoNode and not treeOneNode):
        return False

    if isLeaf(treeOneNode) and isLeaf(treeTwoNode):
        return treeOneNode.val == treeTwoNode.val

    if (isLeaf(treeOneNode) and not isLeaf(treeTwoNode)) or (isLeaf(treeOneNode) and not isLeaf(treeOneNode)):
        return False

    return isSameTreeRecursive(treeOneNode.left, treeTwoNode.left) and treeOneNode.val == treeTwoNode.val and isSameTreeRecursive(treeOneNode.right, treeTwoNode.right)


class Solution:
    def isSameTree(self, p, q):
        return isSameTreeRecursive(p,q)
