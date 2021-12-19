class Solution:
    def allPathsSourceTarget(self, graph):
        self.graph = graph
        self.result = []
        self.backtrack(0, [0])
        return self.result

    def backtrack(self, idx, path):
        if idx == len(self.graph) - 1:
            self.result.append(path)
            return

        for child in self.graph[idx]:
            self.backtrack(child, path + [child])


my_solution = Solution()
print(my_solution.allPathsSourceTarget([[1,2],[3],[3],[]]))
print(my_solution.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
print(my_solution.allPathsSourceTarget([[1],[]]))
print(my_solution.allPathsSourceTarget([[1,2,3],[2],[3],[]]))
print(my_solution.allPathsSourceTarget([[1,3],[2],[3],[]]))