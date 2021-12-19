class Solution:
    def longestOnes(self, nums, k):
        ht = dict()
        ht[0] = 0
        front = 0
        back = 0
        max_length = 0

        while front < len(nums):
            if nums[front] == 0:
                ht[0] += 1
            while ht[0] > k:
                if nums[back] == 0:
                    ht[0] -= 1
                back += 1
            max_length = max(max_length, (front - back) + 1)
            front += 1
        return max_length

my_solution = Solution()
print(my_solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
print(my_solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
print(my_solution.longestOnes([0,0,0,1],0))
print(my_solution.longestOnes([0],0))
