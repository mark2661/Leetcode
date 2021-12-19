
class Solution:
    def strStr(self, haystack, needle):

        if len(needle) > len(haystack):
            return -1

        if len(needle) == 0:
            return 0

        if len(haystack) == 1 and len(needle) == 1:
            return 0 if haystack == needle else -1

        upper_bound = len(needle) - 1
        lower_bound= 0

        while upper_bound < len(haystack):
            if haystack[lower_bound:upper_bound + 1] == needle:
                return lower_bound
            upper_bound += 1
            lower_bound += 1

        return -1

my_solution = Solution()
print(my_solution.strStr("hello","ll"))
print(my_solution.strStr("aaaaa","bba"))
print(my_solution.strStr("",""))
print(my_solution.strStr("abc","c"))
