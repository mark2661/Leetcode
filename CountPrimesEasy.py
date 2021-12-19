


class Solution:
    def countPrimes(self, n):
        count = 0
        lst = [True for n in list(range(2,n))]

        for i in range(2,n):
            if lst[i - 2] == False:
                continue

            current_number = 2 * i
            while current_number < n:
                lst[current_number - 2] = False
                current_number += i
        return len(list(filter(lambda x : not(True and x),lst)))
        #return lst


my_solution = Solution()
print(my_solution.countPrimes(3))