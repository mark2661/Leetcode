
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def getHeight(root):
    if root == None:
        return 0

    max_child_height = 0

    for child in root.children:
        child_height = getHeight(child)
        if child_height > max_child_height:
            max_child_height = child_height

    return 1 + max_child_height

class Solution:
    def maxDepth(self, root):
        return getHeight(root)
