
import sys
# O(n^2) solution (brute force)
# class Solution:
#     def maxProfit(self, prices):
#         best_difference = 0
#         for i in range(len(prices)):
#             for j in range(i,len(prices)):
#                 best_difference = prices[j] - prices[i] if prices[j] - prices[i] > best_difference else best_difference
#
#         return best_difference

#O(n) one pass solution
class Solution:
    def maxProfit(self, prices):
        best_difference = 0
        min_value = sys.maxsize
        for i in range(len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
            elif prices[i] - min_value > best_difference:
                best_difference = prices[i] - min_value
        return best_difference

my_solution = Solution()
print(my_solution.maxProfit([7,1,5,3,6,4]))
print(my_solution.maxProfit([7,6,4,3,1]))