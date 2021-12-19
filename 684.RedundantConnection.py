class Solution:
    def findRedundantConnection(self, edges):
        self.visiting = [0] * len(edges)
        self.dup = set()
        self.ad_list = {j:set() for j in range(1, len(edges)+1)}

        for a,b in edges:
            self.ad_list[a].add(b)
            # self.ad_list[b].add(a)

        self.DFS(1)
        for a,b in edges[-1::-1]:
            if (a,b) in self.dup or (b,a) in self.dup:
                return [a,b]

    def DFS(self, root):
        if self.visiting[root - 1] == -1:
            return True
        if self.visiting[root - 1] == 1:
            return False
        self.visiting[root - 1] = -1
        found = False
        for n in self.ad_list[root]:
            if self.DFS(n) and n != root:
                self.dup.add((root,n))
                found = True

        self.visiting[root - 1] = 1
        return found

my_solution = Solution()
print(my_solution.findRedundantConnection([[1,2],[1,3],[2,3]]))