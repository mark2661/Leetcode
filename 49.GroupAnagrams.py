class Solution:
    def groupAnagrams(self, strs):
        my_dict = dict()
        for word in strs:
            lst = list(word)
            lst.sort()
            sorted_word = "".join(lst)
            if sorted_word in my_dict:
                my_dict[sorted_word].append(word)
            else:
                my_dict[sorted_word] = [word]

        result = []
        for key in my_dict.keys():
            result.append(my_dict[key])
        return result




my_solution = Solution()
print(my_solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(my_solution.groupAnagrams([""]))
print(my_solution.groupAnagrams(["a"]))
