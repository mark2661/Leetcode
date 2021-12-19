

def gen_brackets(n, left_rem, right_rem, s):
    if len(s) == n * 2:
        return [s]
    result = []

    if left_rem > 0:
        result = result + gen_brackets(n, left_rem - 1, right_rem, s + "(")
    if left_rem < right_rem:
        result = result + gen_brackets(n, left_rem, right_rem - 1, s + ")")

    return result

class Solution:
    def generateParenthesis(self, n):
        return gen_brackets(n, n, n, "")


my_solution = Solution()
print(my_solution.generateParenthesis(1))
print(my_solution.generateParenthesis(3))

