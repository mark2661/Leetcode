class Solution:
    def maxSubArray(self, nums):

        sum = nums[0]
        best = nums[0]

        for i in range(1,len(nums)):
            sum = max(nums[i],sum + nums[i])
            best = max(sum,best)

        return best

my_solution = Solution()
print(my_solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(my_solution.maxSubArray([1]))
print(my_solution.maxSubArray([-1]))