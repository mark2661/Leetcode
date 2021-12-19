# import sys
#
#
# class Solution:
#     def coinChange(self, coins, amount):
#         self.memo = dict()
#         self.coins = coins
#         result = self.CC(amount)
#         return result if result < sys.maxsize else -1
#
#     def CC(self,amount):
#         if amount in self.memo:
#             return self.memo[amount]
#         if amount == 0:
#             return 0
#         if amount < 0:
#             return sys.maxsize
#
#         num_ways = sys.maxsize
#         for coin in self.coins:
#             num_ways = min(num_ways, self.CC(amount - coin))
#         self.memo[amount] = (1 + num_ways) if num_ways < sys.maxsize else sys.maxsize
#         return self.memo[amount]

import sys


class Solution:
    def coinChange(self, coins, amount):
        arr = [amount + 1] * (amount + 1)
        arr[0] = 0
        for i in range(1,len(arr)):
            for coin in coins:
                if i - coin >= 0:
                    arr[i] = min(arr[i], arr[i - coin] + 1)
        return arr[amount] if arr[amount] != amount + 1 else -1



my_solution = Solution()
print(my_solution.coinChange([1,2,5],11))
print(my_solution.coinChange([2],3))
print(my_solution.coinChange([1],0))
print(my_solution.coinChange([1],1))
print(my_solution.coinChange([1],2))
