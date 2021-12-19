
# class Solution:
#     def plusOne(self, digits):
#
#         for i in range(len(digits) - 1, 0, -1):
#             if digits[i] != 9:
#                 digits[i] += 1
#                 return digits
#             elif digits[i] == 9 and i > 1:
#                 digits[i] = 0
#
#         return [1] + [0] * len(digits) if digits[0] == 9 else [digits[0] + 1] + ([0] * (len(digits) -1))


class Solution:
    def plusOne(self, digits):

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            elif digits[i] == 9:
                digits[i] = 0

        return [1] + digits



my_solution = Solution()
print(my_solution.plusOne([0]))
print(my_solution.plusOne([9,8,9]))
print(my_solution.plusOne([9,9]))
print(my_solution.plusOne([9,9,9]))