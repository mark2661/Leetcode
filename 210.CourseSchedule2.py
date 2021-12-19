from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        if len(prerequisites) == 0:
            return [n for n in range(numCourses)]
        self.course_order = []
        self.ad_list = dict()
        self.visited = [0] * numCourses
        self.st = deque()
        self.is_possible = True

        for a,b in prerequisites:
            if b in self.ad_list:
                self.ad_list[b].append(a)
            else:
                self.ad_list[b] = [a]

        for i in range(len(self.visited)):
            self.DFS(i)

        while len(self.st) > 0:
            self.course_order.append(self.st.pop())

        return self.course_order if self.is_possible else []

    def DFS(self, root):
        if not self.is_possible:
            return
        if self.visited[root] == 1:
            return
        if self.visited[root] == -1:
            self.is_possible = False
            return
        self.visited[root] = -1
        if root in self.ad_list:
            for n in self.ad_list[root]:
                self.DFS(n)
        self.visited[root] = 1
        self.st.append(root)
        return
