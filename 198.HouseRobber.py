# class Solution:
#     def rob(self, nums):
#         self.nums = nums
#         self.memo = dict()
#         result = 0
#         for i in range(len(nums)):
#             result = max(result, self.rb(i))
#         return result
#     def rb(self, start):
#         if start in self.memo:
#             return self.memo[start]
#         money = 0
#         for i in range(start + 2, len(self.nums)):
#             money = max(money, self.rb(i))
#         self.memo[start] = self.nums[start] + money
#         return self.memo[start]

class Solution:
    def rob(self, nums):
        for i in range(len(nums) - 3,-1,-1):
            nums[i] += max(nums[i+2:])

        return max(nums)