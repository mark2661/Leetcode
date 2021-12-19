class Solution:
    def getSum(self, a, b):
        addition = a ^ b
        carry = a & b
        if carry == 0:
            return addition
        carry = carry << 1
        while True:
            old_carry, old_addition = carry, addition
            addition = old_addition ^ old_carry
            carry = old_addition & old_carry
            if carry == 0:
                break
            else:
                carry = carry << 1
        return addition

my_solution = Solution()
print(my_solution.getSum(-1,1))