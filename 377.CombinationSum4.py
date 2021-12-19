# class Solution:
#     def combinationSum4(self, nums, target):
#         self.nums = nums
#         self.memo = dict()
#         return self.CS(target)
#
#     def CS(self, target):
#         if target in self.memo:
#             return self.memo[target]
#         if target == 0:
#             return 1
#         if target < 0:
#             return 0
#         num_ways = 0
#         for n in self.nums:
#             num_ways += self.CS(target - n)
#         self.memo[target] = num_ways
#         return self.memo[target]

class Solution:
    def combinationSum4(self, nums, target):
        arr = [0] * (target + 1)
        arr[0] = 1

        for i in range(len(arr)):
            for n in nums:
                if i - n >= 0:
                    arr[i] += arr[i-n]
        return arr[target]
