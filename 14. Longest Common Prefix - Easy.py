

# class Solution:
#     def longestCommonPrefix(self, strs):
#
#         strs.sort(key = len)
#         prefix = strs[0] if len(strs) > 0 else ""
#
#         while len(prefix) > 0:
#             found = True
#             for word in strs:
#                 if word[0:len(prefix)] != prefix:
#                     prefix = prefix[:-1]
#                     found = False
#                     break
#             if(found):
#                 return prefix
#
#         return prefix

def longestPrefix(str_one,str_two = ""):
    if str_two == "":
        return str_two

    length = min(len(str_one),len(str_two))
    prefix = ""
    for i in range(length):
        if str_one[i] == str_two[i]:
            prefix += str_one[i]
        else:
            return prefix
    return prefix

class Solution:
    def longestCommonPrefix(self, strs):

        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        elif len(strs) == 2:
            return longestPrefix(strs[0],strs[1])

        mid = len(strs) // 2

        return longestPrefix(self.longestCommonPrefix(strs[:mid]),self.longestCommonPrefix(strs[mid:]))




my_solution = Solution()
print(my_solution.longestCommonPrefix(["flower","flow","flight"]))
print(my_solution.longestCommonPrefix(["dog","racecar","car"]))
print("")

#print(longestPrefix("lee","le"))