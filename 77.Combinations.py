
def combo(n, k):
    if n == 0:
        return [[]]

    comboWithoutN = combo(n - 1, k)
    comboWithN = []

    for com in comboWithoutN:
        if len(com) < k:
            comboWithN.append(com + [n])

    return [] + comboWithoutN + comboWithN

class Solution:
    def combine(self, n, k):
        return [n for n in combo(n, k) if len(n) == k]


my_solution = Solution()
print(my_solution.combine(4,2))
print(my_solution.combine(1,1))