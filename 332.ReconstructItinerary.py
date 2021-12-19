class Solution:
    def findItinerary(self, tickets):
        self.result = []
        self.ad_list = dict()
        self.keys = set()

        for f, t in tickets:
            self.keys.add(f)
            if f not in self.ad_list:
              self.ad_list[f] = set()
            self.ad_list[f].add(t)

        self.DFS("JFK",[])
       # print(self.result)
        if len(self.result) != 1:
            self.result.sort()
        return self.result[0]

    def DFS(self,root,path):
        if len(self.keys) == 0:
            path = path + [root]
            self.result.append(path)
            return

        if root not in self.ad_list or len(self.ad_list[root]) == 0:
            return

        for n in self.ad_list[root]:
            self.ad_list[root].remove(n)
            if len(self.ad_list[root]) == 0:
                self.keys.remove(root)
            self.DFS(n,path + [root])
            self.ad_list[root].add(n)
            if root not in self.keys:
                self.keys.add(root)

        return


my_solution = Solution()
print(my_solution.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))