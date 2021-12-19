
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        self.result = [[root.val]]
        self.q = [root]
        self.BFS()
        return self.result

    def BFS(self):
        while len(self.q) > 0:
            new_level = []
            for n in self.q:
                for c in n.children:
                    new_level.append(c)
            if len(new_level) > 0:
                self.result.append([n.val for n in new_level])
            self.q = new_level
