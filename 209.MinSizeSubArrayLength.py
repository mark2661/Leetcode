import sys

class Solution:
    def minSubArrayLen(self, target, nums):
        currentSum = 0
        frontPointer = 0
        backPointer = 0
        min_length = sys.maxsize

        while frontPointer < len(nums):
            currentSum += nums[frontPointer]
            frontPointer += 1
            if currentSum < target:
                continue
            else:
                while currentSum >= target and backPointer <= frontPointer:
                    min_length = min(min_length, frontPointer - backPointer)
                    currentSum -= nums[backPointer]
                    backPointer += 1

        return min_length if min_length != sys.maxsize else 0

my_solution = Solution()
print(my_solution.minSubArrayLen(7, [2,3,1,2,4,3]))
print(my_solution.minSubArrayLen(4, [1,4,4]))
print(my_solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
print(my_solution.minSubArrayLen(11,[1,2,3,4,5]))