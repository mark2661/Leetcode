# class Solution:
#     def sortColors(self, nums):
#         for i in range(len(nums)-1, -1, -1):
#             swapped = False
#             for j in range(0, i):
#                 if nums[j] > nums[j+1]:
#                     nums[j], nums[j+1] = nums[j+1], nums[j]
#                     swapped = True
#             if not swapped:
#                 break
#         return nums

class Solution:
    def sortColors(self, nums):
        c0 = c1 = c2 = 0
        for n in nums:
            if n == 0:
                c0 += 1
            elif n == 1:
                c1 += 1
            else:
                c2 += 1
        nums[0:c0] = [0] * c0
        nums[c0:c1+1] = [1] * c1
        nums[c1+1:c2+1] = [2] * c2
        return nums

