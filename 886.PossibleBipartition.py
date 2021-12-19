# class Solution:
#     def possibleBipartition(self, n, dislikes):
#         self.ad_list = {j:[] for j in range(1,n+1)}
#         self.groups = [0] * n
#         self.visiting = [0] * n
#
#         for a, b in dislikes:
#             self.ad_list[a].append(b)
#             self.ad_list[b].append(a)
#
#         for j in range(1, n+1):
#             if self.visiting[j - 1] != 1 and not self.DFS(j, -1):
#                 return False
#         return True
#
#     def DFS(self,root,group):
#         if self.visiting[root - 1] == 1:
#             return group != self.groups[root - 1]
#         if self.groups[root - 1] == group:
#             return False
#         group = -1 * group
#         self.groups[root - 1] = group
#         self.visiting[root - 1] = -1
#
#         self.visiting[root - 1] = -1
#         for n in self.ad_list[root]:
#             if self.visiting[n - 1] == -1:
#                 continue
#             if not self.DFS(n,group):
#                 self.visiting[root - 1] = 1
#                 return False
#         self.visiting[root - 1] = 1
#         return True

class Solution:
    def possibleBipartition(self, n, dislikes):
        self.ad_list = {j:[] for j in range(1,n+1)}
        self.visiting = [0] * n

        for a, b in dislikes:
            self.ad_list[a].append(b)
            self.ad_list[b].append(a)

        for j in range(1, n+1):
            if self.visiting[j - 1] == 0 and not self.DFS(j, 1):
                return False
        return True

    def DFS(self,root,group):
        self.visiting[root - 1] = group

        for n in self.ad_list[root]:
            if self.visiting[n - 1] == group:
                return False
            if self.visiting[n - 1] == 0 and not self.DFS(n,-group):
                return False
        return True

