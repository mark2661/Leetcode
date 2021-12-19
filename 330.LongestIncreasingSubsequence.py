class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 1:
            return 1
        arr = [1] * len(nums)
        idx = len(nums) - 2
        longest = 1

        while idx > -1:
            best = 0
            for i in range(idx + 1, len(nums)):
                if nums[i] > nums[idx]:
                    best = max(best, arr[i])
            arr[idx] = best + 1
            longest = max(longest, arr[idx])
            idx -= 1

        return longest

my_solution = Solution()
print(my_solution.lengthOfLIS([0,1,0,3,2,3]))