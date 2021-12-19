class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        current_prod = 1
        front = 0
        back = 0
        num_arrays = 0

        while front < len(nums):

            current_prod *= nums[front]

            if current_prod >= k:
                while current_prod >= k and back <= front:
                    current_prod = current_prod // nums[back]
                    if nums[back] < k:
                        num_arrays += 1
                    back += 1
            if current_prod < k:
                num_arrays += 1
            front += 1


        while back < front:
            current_prod = current_prod // nums[back]
            back += 1
            if current_prod < k:
                num_arrays += 1

        return num_arrays

my_solution = Solution()
print(my_solution.numSubarrayProductLessThanK([10,5,2,6],100))
print(my_solution.numSubarrayProductLessThanK([1,2,3],0))
print(my_solution.numSubarrayProductLessThanK([10,9,10,4,3,8,3,3,6,2,10,10,9,3],19))