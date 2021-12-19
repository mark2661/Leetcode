from queue import Queue

def bfs(node):
    q = Queue()
    q.put(node)
    stop = False
    while(not q.empty()):
            node = q.get()
            print(node.val)
            if node.left != None:
                q.put(node.left)
            if node.right != None:
                q.put(node.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

my_binary_tree = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))
bfs(my_binary_tree)