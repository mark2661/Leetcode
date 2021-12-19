class Solution:
    def missingNumber(self, nums):

        full_set = set(range(0, len(nums) + 1))
        nums_set = set(nums)
        
        return list(full_set.difference(nums_set))[0]

my_solution = Solution()
my_solution.missingNumber([0,1])
my_solution.missingNumber([3,0,1])