
# def binary_search_recursive(array,element,start,end):
#     if start > end:
#         return -1
#
#     mid = (start + end) // 2
#     if array[mid] == element:
#         return mid
#     if element < array[mid]:
#         return binary_search_recursive(array,element,start,mid-1)
#     else:
#         return binary_search_recursive(array, element, mid + 1, end)
#
# class Solution:
#     def singleNumber(self, nums):
#         nums.sort() # O(n * log n)
#         if len(nums) == 1:
#             return nums[0]
#         my_dict = dict()
#         for i in range(len(nums)): # o(n)
#             if my_dict.get(nums[i]) != None:
#                 continue
#             if binary_search_recursive(nums,nums[i],i+1,len(nums) - 1) != -1: # O(log n)
#                 my_dict[nums[i]] = True
#             else:
#                 return nums[i]

class Solution:
    def singleNumber(self, nums):
        # o(n) solution
        my_dict = dict()
        for number in nums:
            if my_dict.get(number) != None:
                my_dict[number] += 1
            else:
                my_dict[number] = 1
        for key in my_dict.keys():
            if my_dict[key] == 1:
                return key


my_solution = Solution()
print(my_solution.singleNumber([2,2,1]))
print(my_solution.singleNumber([4,1,2,1,2]))
print(my_solution.singleNumber([1,1,2,3,4,5,4,5,3,-1,2]))
