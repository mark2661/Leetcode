class Solution:
    def reverseBits(self, n: int):
        reverse = 0
        shift = 32

        while n:
            digit = n & 1
            shift -= 1

            curr = digit << shift
            reverse = reverse | curr
            n = n >> 1
        return reverse