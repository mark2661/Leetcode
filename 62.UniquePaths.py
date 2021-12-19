# class Solution:
#     def uniquePaths(self, m, n):
#         self.memo = dict()
#         return self.UP(m, n)
#
#     def UP(self, m, n):
#         if m == 1 or n == 1:
#             return 1
#         if (m, n) in self.memo:
#             return self.memo[(m, n)]
#
#         self.memo[(m, n)] = self.UP(m - 1, n) + self.UP(m, n - 1)
#         return self.memo[(m, n)]


class Solution:
    def uniquePaths(self, m, n):
        grid = [[0] * n] * m
        #set last row to 1's
        grid[-1] = [1] * n
        #set last column to 1's
        for row in grid:
            row[-1] = 1

        # start at cell in penultimate column of the penultimate row (since outside is initialised to 1's)
        for row in range(m-2,-1,-1):
            for col in range(n-2,-1,-1):
                grid[row][col] = grid[row+1][col] + grid[row][col+1]
        return grid[0][0]




# my_solution = Solution()
# my_solution.uniquePaths(3,3)