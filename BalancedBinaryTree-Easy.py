#import sys
from queue import Queue
# def balanced(root,count):
#     if root == None:
#         return sys.maxsize if count != 0 else 0
#     count += 1
#     if isLeaf(root):
#         return count
#     return min(balanced(root.left,count),balanced(root.right,count))

def bfs(node):
    q = Queue()
    q.put(node)
    stop = False
    depth = 1
    while(not stop):
        if q.empty():
            return depth
        current_length = q.qsize()
        for i in range(current_length):
            node = q.get()
            if(isLeaf(node)):
                return depth
            if(node.left != None):
                q.put(node.left)
            if(node.right != None):
                q.put(node.right)
        depth += 1



def isLeaf(root):
    return root.left == None and root.right == None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root):
        if root == None:
            return 0
        return bfs(root)