class Solution:
    def canFinish(self, numCourses, prerequisites):
        if len(prerequisites) < 2:
            return True
        self.ad_list = dict()
        self.visited = [0] * numCourses

        for l in prerequisites:
            if l[0] in self.ad_list:
                self.ad_list[l[0]].append(l[1])
            else:
                self.ad_list[l[0]] = [l[1]]

        for key in self.ad_list.keys():
            if not self.DFS(key):
                return False
        return True

    def DFS(self,root):
        if root not in self.ad_list:
            return True
        if self.visited[root] == 1:
            return True
        if self.visited[root] == -1:
            return False

        self.visited[root] = -1
        for n in self.ad_list[root]:
            if not self.DFS(n):
                return False
        self.visited[root] = 1
        return True
