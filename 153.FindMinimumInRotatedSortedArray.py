# class Solution:
#     def findMin(self, nums):
#         if len(nums) == 1:
#             return nums[0]
#         left, right = 0, len(nums) - 1
#         while True:
#             mid = (left + right) // 2
#             if left == mid or right == mid:
#                 return min(nums[left],nums[right])
#             #Entire array is sorted
#             if nums[mid] >= nums[left] and nums[mid] < nums[right]:
#                 return nums[left]
#             #Left side of array is sorted
#             if nums[mid] >= nums[left]:
#                 left = mid
#             #Right side of the array is sorted
#             else:
#                 right = mid

# class Solution:
#     def findMin(self, nums):
#         if len(nums) == 1:
#             return nums[0]
#         left, right = 0, len(nums) - 1
#         if nums[left] < nums[right]:
#             return nums[left]
#         while left < right:
#             mid = (left + right) // 2
#             if nums[mid - 1] > nums[mid]:
#                 return nums[mid]
#             if nums[mid] > nums[mid+1]:
#                 return nums[mid+1]
#             #left sorted
#             if nums[left] <= nums[mid]:
#                 left = mid + 1
#             #right sorted
#             else:
#                 right = mid - 1

class Solution:
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        minVal = 5000

        while left <= right:
            if nums[left] < nums[right]:
                return min(minVal,nums[left])
            mid = (left + right) // 2
            minVal = min(minVal, nums[mid])
            #left sorted
            if nums[left] <= nums[mid]:
                left = mid + 1
            #right sorted
            else:
                right = mid - 1
        return minVal
