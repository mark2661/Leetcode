#Recursive top down DP solution
# class Solution:
#     def canJump(self, nums):
#         self.memo = dict()
#         self.nums = nums
#         return self.CJ(0)
#
#     def CJ(self,idx):
#         if idx in self.memo:
#             return self.memo[idx]
#         if idx == len(self.nums) - 1:
#             return True
#         if idx >= len(self.nums):
#             return False
#
#         for jump in range(1, self.nums[idx] + 1):
#             if self.CJ(idx + jump):
#                 return True
#
#         self.memo[idx] = False
#         return False

# Iterative bottom up DP solution with boolean array
# class Solution:
#     def canJump(self, nums):
#         if len(nums) == 1:
#             return True
#         arr = [False] * len(nums)
#         arr[-1] = True
#         idx = len(arr) - 2
#         min_true = len(arr) - 1
#
#         while idx > -1:
#             if idx < min_true <= idx + nums[idx]:
#                 #arr[idx] = True
#                 min_true = idx
#             idx -= 1
#         return arr[0]

#Iterative bottom up DP solution without array
class Solution:
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        idx = len(nums) - 2
        min_true = len(nums) - 1

        while idx > -1:
            if idx < min_true <= idx + nums[idx]:
                min_true = idx
            idx -= 1
        return min_true == 0

# my_solution = Solution()
# print(my_solution.canJump([3,2,1,0,4]))
