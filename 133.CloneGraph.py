
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None
        self.adList = dict()
        self.DFS(node)
        return self.adList[1]

    def DFS(self,root):
        self.adList[root.val] = Node(root.val)

        for neighbour in root.neighbors:
            if neighbour.val not in self.adList:
                self.DFS(neighbour)

            self.adList[root.val].neighbors.append(self.adList[neighbour.val])

my_solution = Solution()
one = Node(1)
two = Node(2)
one.neighbors.append(two)
two.neighbors.append(one)
my_solution.cloneGraph(one)

