import sys

#O(n) one pass solution
class Solution:
    def maxProfit(self, prices):
        profit = 0

        if len(prices) == 0 or len(prices) == 1:
            return profit

        current = 0
        has_stock = False

        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i] and not has_stock: #If price after is higher buy the current stock
                current = prices[i]
                has_stock = True
            elif prices[i+1] < prices[i] and has_stock: #If price after drops sell current stock
                profit += prices[i] - current
                has_stock = False

        profit = profit + (prices[-1] - current) if prices[-1] - current > 0 and has_stock else profit #decision weather or not you should sell
                                                                                                        #on the last day
        return profit

my_solution = Solution()
print(my_solution.maxProfit([7,1,5,3,6,4]))
print(my_solution.maxProfit([1,2,3,4,5]))
print(my_solution.maxProfit([7,6,4,3,1]))


