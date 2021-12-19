# class Solution:
#     def twoSum(self, nums, target):
#         new_list = nums.copy()
#         new_list.sort()
#         for elem in nums:
#             idx = binary_search_recursive(nums,(target-elem),0,len(nums))
#             if idx > -1:
#                 return [nums.index(elem), idx]

# class Solution:
#     def twoSum(self, nums, target):
#         my_dict = dict()
#
#         for i in range(len(nums)):
#             compliment = target - nums[i]
#             if(compliment in my_dict.keys()):
#                 return [my_dict[compliment], i]
#             my_dict[nums[i]] = i

class Solution:
    def twoSum(self, nums, target):
        my_dict = dict()
        for i,v in enumerate(nums):
            compliment = target - v
            if(compliment in my_dict.keys()):
                return [my_dict[compliment], i]
            my_dict[v] = i






def binary_search_recursive(lst, value,start,end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if value == lst[mid]:
        return mid
    if value < lst[mid]:
        return binary_search_recursive(lst, value, start, mid - 1)
    else:
        return binary_search_recursive(lst, value, mid + 1, end)

my_solution = Solution()
print(my_solution.twoSum([2,7,11,15],9))
print(my_solution.twoSum([3,2,4],6))
print(my_solution.twoSum([3,3],6))