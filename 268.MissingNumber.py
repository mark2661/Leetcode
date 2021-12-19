class Solution:
    def missingNumber(self, nums):
        expectedVal = (len(nums) / 2) * (len(nums) + 1)
        return int(expectedVal) - sum(nums)

