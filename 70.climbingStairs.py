class Solution:
    def climbStairs(self, n):
        self.memo = dict()
        return self.csr(n)

    def csr(self,n):
        if n in self.memo:
            return self.memo[n]
        if n == 1:
            return 1
        if n == 0:
            return 1
        self.memo[n] = self.csr(n-1) + self.csr(n-2)
        return self.memo[n]