

class Solution:
    def reverse(self, x):
        if x >= 0:
            return int(str(x)[-1::-1]) if pow(-2, 31) < int(str(x)[-1::-1]) < pow(2, 31) - 1 else 0
        else:
            return int("-" + str(x)[-1:0:-1]) if pow(-2, 31) < int("-" + str(x)[-1:0:-1]) < pow(2, 31) - 1 else 0


my_solution = Solution()
print(my_solution.reverse(123))
print(my_solution.reverse(-123))
print(my_solution.reverse(120))
print(my_solution.reverse(0))