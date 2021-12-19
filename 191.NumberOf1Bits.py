class Solution:
    def hammingWeight(self, n: int) -> int:
        # count = 0
        # #n = bin(n)
        # for i in range(32):
        #     if n & (1 << i) != 0:
        #         count += 1
        # return count

        count = 0
        while n != 0:
            count += n & 1
            n = n >> 1
        return count
