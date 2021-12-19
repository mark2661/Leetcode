import sys


# class Solution:
#     def findMinHeightTrees(self, n, edges):
#         self.min_height_trees = []
#         self.ad_list = {j:[] for j in range(n)}
#         self.heights = [0] * n
#         self.visting = [0] * n
#         self.memo = dict()
#
#         for a,b in edges:
#             self.ad_list[a].append(b)
#             self.ad_list[b].append(a)
#         for i in range(len(self.heights)):
#             self.heights[i] = self.get_height(i)
#         min_h = min(self.heights)
#         for i in range(len(self.heights)):
#             if self.heights[i] == min_h:
#                 self.min_height_trees.append(i)
#         return self.min_height_trees
#
#     def get_height(self,root):
#         max_child = -1
#         self.visting[root] = -1
#         for n in self.ad_list[root]:
#             if self.visting[n] == 0:
#                 max_child = max(max_child,self.get_height(n))
#         self.visting[root] = 0
#         return 1 + max_child

class Solution:
    def findMinHeightTrees(self, n, edges):
        self.min_height_trees = []
        self.ad_list = {j:[] for j in range(n)}
        self.num_nodes = n

        for a,b in edges:
            self.ad_list[a].append(b)
            self.ad_list[b].append(a)
        # for a,b in self.ad_list.items():
        #     print(a,b)
        leaves = []
        for n in self.ad_list.keys():
            if len(self.ad_list[n]) == 1:
                leaves.append(n)

        nodes_rem = self.num_nodes
        while nodes_rem > 2:
            nodes_rem -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                n = self.ad_list[leaf][0]
                self.ad_list[n].remove(leaf)
                del self.ad_list[leaf]
                if len(self.ad_list[n]) == 1:
                    new_leaves.append(n)

            leaves = new_leaves

        for key in self.ad_list.keys():
            self.min_height_trees.append(key)
            print(key)

        return self.min_height_trees


my_solution = Solution()
print(my_solution.findMinHeightTrees(3, [[0,1],[0,2]]))

