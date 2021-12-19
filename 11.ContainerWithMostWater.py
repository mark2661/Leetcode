# class Solution:
#     def maxArea(self, height):
#         if len(height) == 2:
#             return min(height[0], height[1])
#
#
#         max_height = -1
#         max_idx = 0
#         for i in range(len(height)):
#             if height[i] > max_height:
#                 max_height = height[i]
#                 max_idx = i
#
#         left, right = 0, len(height) - 1
#         max_area = max(min(height[left], height[right]) * (right - left),
#                        height[left] * abs(max_idx - left),
#                        height[right] * abs(right - max_idx))
#
#
#         while left < right:
#             max_area = max(min(height[left], height[right]) * (right - left),
#                            height[left] * abs(max_idx - left),
#                            height[right] * abs(right - max_idx), max_area)
#
#             if height[left] <= height[right]:
#                 left += 1
#             else:
#                 right -= 1
#
#         return max_area

# my_solution = Solution()
# print(my_solution.maxArea([1,8,6,2,5,4,8,3,7]))

class Solution:
    def maxArea(self, height):
        if len(height) == 2:
            return min(height[0], height[1])

        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] <= height[right]:
                max_area = max(max_area, min(height[left], height[right]) * (right - left))
                left += 1
            else:
                max_area = max(max_area, min(height[left], height[right]) * (right - left))
                right -= 1
        return max_area


        return max_area
