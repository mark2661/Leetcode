#
#
# class Solution:
#     def removeDuplicates(self, nums):
#
#         if len(nums) < 2:
#             return len(nums)
#         elif len(nums) == 2:
#             return len(nums) if nums[0] != nums[1] else 1
#
#         lag_pointer = 0
#         lead_pointer = 1
#
#         while(lag_pointer < len(nums) - 1):
#
#             while (nums[lead_pointer] == nums[lag_pointer]):
#                 if lead_pointer < len(nums) - 1:
#                     lead_pointer += 1
#                 else:
#                     del nums[lag_pointer + 1:]
#                     break
#             del nums[lag_pointer + 1: lead_pointer]
#             lag_pointer += 1
#             lead_pointer = lag_pointer + 1
#
#         if len(nums) == 2:
#             return len(nums) if nums[0] != nums[1] else 1
#         #print(nums)
#         return len(nums)


class Solution:
    def removeDuplicates(self, nums):

        if len(nums) < 2:
            return len(nums)
        elif len(nums) == 2:
            return len(nums) if nums[0] != nums[1] else 1

        lag_pointer = 0
        # lead_pointer = 1

        for lead_pointer in range(1,len(nums)):
            if nums[lead_pointer] == nums[lag_pointer]:
                continue
            nums[lag_pointer +  1] = nums[lead_pointer]
            lag_pointer += 1

        del nums[lag_pointer + 1:]

        return len(nums)




my_solution = Solution()
print(my_solution.removeDuplicates([1,1,2]))
print(my_solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(my_solution.removeDuplicates([1,1,1]))
print(my_solution.removeDuplicates([1,2,2]))

