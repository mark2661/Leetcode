


class Solution:
    def isAnagram(self, s,t):
        my_dict = dict()
        for letter in s:
            my_dict[letter] = my_dict[letter] + 1 if letter in my_dict.keys() else 1

        for letter in t:
            if letter not in my_dict.keys():
                return False
            my_dict[letter] = my_dict[letter] - 1

        return sum([abs(n) for n in my_dict.values()]) == 0

my_solution = Solution()
print(my_solution.isAnagram("anagram","nagaram"))
print(my_solution.isAnagram("rat","car"))
print(my_solution.isAnagram("a","ab"))
print(my_solution.isAnagram("aacc","ccac"))