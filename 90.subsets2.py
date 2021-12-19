class Solution:
    def subsetsWithDup(self, nums):
        self.result = []
        self.nums = nums
        self.nums.sort()
        self.backtrack(len(nums), [], 0)
        return self.result

    def backtrack(self, n, state, idx):
        if idx > len(self.nums):
            return
        self.result.append(state)

        for i in range(idx, len(self.nums)):
            if(i == idx or self.nums[i] != self.nums[i-1]):
                self.backtrack(n, state + [self.nums[i]], i + 1)



my_solution = Solution()
print(my_solution.subsetsWithDup([1,2,2]))
print(my_solution.subsetsWithDup([0]))