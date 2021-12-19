def count_routes(n, memo):
    if memo[n] > 0:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    memo[n] = count_routes(n - 1, memo) + count_routes(n - 2, memo)
    return memo[n]


class Solution:
    def climbStairs(self, n):
        memo = dict()
        for i in range(1, n+1):
            memo[i] = 0
        return count_routes(n, memo)

my_solution = Solution()
print(my_solution.climbStairs(4))