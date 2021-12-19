class Solution:
    def findTargetSumWays(self, nums, target):
        self.max_idx = len(nums)
        self.target = target
        self.nums = nums
        self.memo = dict()


        return self.backtrack(0, 0)

    def backtrack(self, idx, total):
        if (idx, total) in self.memo:
            return self.memo[(idx, total)]

        if idx == self.max_idx:
            if total == self.target:
                return 1
            else:
                return 0

        ans = self.backtrack(idx + 1, total + self.nums[idx]) + self.backtrack(idx + 1, total + (self.nums[idx] * -1))
        self.memo[(idx, total)] = ans
        return ans

my_solution = Solution()
print(my_solution.findTargetSumWays([1,1,1,1,1], 3))
print(my_solution.findTargetSumWays([1], 1))
print(my_solution.findTargetSumWays([20,48,33,16,19,44,14,31,42,34,38,32,27,7,22,22,48,18,48,39],1))