class Solution:
    def combinationSum3(self, k, n):
        self.lst = list(range(1, 10))
        self.result = []
        self.max_depth = k

        for x in range(len(self.lst)):
            self.backtrack(1, n - self.lst[x], [self.lst[x]], x + 1)
        return self.result

    def backtrack(self, depth, n, path, idx):
        if depth > self.max_depth:
            return
        if n == 0 and depth == self.max_depth:
            self.result.append(path)
            return

        for i in range(idx, len(self.lst)):
            self.backtrack(depth + 1, n - self.lst[i], path + [self.lst[i]], i + 1)


my_solution = Solution()
print(my_solution.combinationSum3(3,7))
print(my_solution.combinationSum3(3,9))
print(my_solution.combinationSum3(4,1))
print(my_solution.combinationSum3(9,45))