class Solution:
    def isBipartite(self, graph):
        self.ad_list = dict()

        for i in range(len(graph)):
            self.ad_list[i] = graph[i]

        self.visiting = [0] * len(self.ad_list)

        for j in range(len(self.ad_list)):
            if self.visiting[j] == 0 and not self.DFS(j, 1):
                return False
        return True

    def DFS(self,root, group):
        self.visiting[root] = group

        for n in self.ad_list[root]:
            if self.visiting[n] == group:
                return False
            if self.visiting[n] == 0 and not self.DFS(n,-group):
                return False
        return True
