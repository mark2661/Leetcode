# class Solution:
#     def maxProduct(self, nums):
#         if len(nums) == 1:
#             return nums[0]
#
#         q = []
#         for j in range(len(nums)):
#             if nums[j] <= 0:
#                 q.append(nums[j])
#
#         current_prod = nums[0]
#         max_prod = nums[0]
#         i = 1
#         while i < len(nums):
#             if nums[i] <= 0:
#                 q.pop(0)
#             if nums[i] == 0:
#                 max_prod = max(max_prod, current_prod, 0)
#                 if i < len(nums) - 1:
#                     current_prod = nums[i + 1]
#                     i += 2
#                 else:
#                     break
#
#             elif current_prod * nums[i] >= nums[i]:
#                 max_prod = max(max_prod, current_prod, current_prod * nums[i])
#                 current_prod *= nums[i]
#                 i += 1
#             else:
#                 max_prod = max(max_prod, current_prod)
#                 if len(q) > 0 and q[0] < 0:
#                     current_prod *= nums[i]
#                 else:
#                     current_prod = nums[i]
#                 i += 1
#
#         return max(max_prod, current_prod)
#
# my_solution = Solution()
# print(my_solution.maxProduct([2,3,-2,4]))
# print(my_solution.maxProduct([-2,0,-1]))
# print(my_solution.maxProduct([0,2]))
#

class Solution:
    def maxProduct(self, nums):
        if len(nums) == 1:
            return nums[0]
        local_min = local_max = 1
        global_max = max(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                local_min = local_max = 1
                #global_max = max(global_max, local_max)
            else:
                temp = local_max
                local_max = max(temp * nums[i], local_min * nums[i], nums[i])
                local_min = min(temp * nums[i], local_min * nums[i], nums[i])
                global_max = max(global_max, local_max)

        return global_max

my_solution = Solution()
print(my_solution.maxProduct([2,3,-2,4]))
print(my_solution.maxProduct([-2,0,-1]))
print(my_solution.maxProduct([0,2]))

