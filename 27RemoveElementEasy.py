

# class Solution:
#     def removeElement(self, nums, val):
#
#         if len(nums) == 0:
#             return len(nums)
#
#         if len(nums) == 1 and nums[0] == val:
#             return 0
#
#         if len(nums) == 1:
#             return len(nums)
#
#         end_pointer = len(nums) - 1
#
#         for start_pointer in range(len(nums)):
#
#             if start_pointer > end_pointer:
#                 break
#
#             while(nums[end_pointer] == val):
#                 if end_pointer > 0:
#                     end_pointer -= 1
#                 else:
#                     return 0
#
#             # if start_pointer > end_pointer:
#             #     break
#
#             #end_pointer += 1
#
#             if nums[start_pointer] == val:
#                 nums[start_pointer],nums[end_pointer] = nums[end_pointer],nums[start_pointer]
#                 end_pointer -= 1
#
#
#         # del nums[start_pointer:]
#         #print(nums)
#         if start_pointer == len(nums) - 1:
#             return len(nums)
#         return len(nums[:start_pointer])

class Solution:
    def removeElement(self, nums, val):

        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

my_solution= Solution()
print(my_solution.removeElement([3,2,2,3],3))