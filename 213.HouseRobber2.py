class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        withOutFirst = nums[1:]
        withOutLast = nums[:len(nums) - 1]
        for i in range(len(withOutFirst) - 3, -1, -1):
            withOutFirst[i] += max(withOutFirst[i + 2:])
        for i in range(len(withOutLast) - 3, -1, -1):
            withOutLast[i] += max(withOutLast[i + 2:])

        return max(max(withOutFirst),max(withOutLast))
