# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 1:
#             return 1
#         char_set = set()
#         current_string = ""
#         longest = 0
#         i = 0
#         while i < len(s):
#             if s[i] not in char_set:
#                 current_string += s[i]
#                 char_set.add(s[i])
#                 i += 1
#             else:
#                 longest = len(current_string) if len(current_string) > longest else longest
#                 #current_string = "" + s[i]
#                 current_string = ""
#                 char_set.clear()
#                 #char_set.add(s[i])
#                 i -= 1
#
#         longest = len(current_string) if len(current_string) > longest else longest
#         return longest

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 1:
#             return 1
#         char_set = dict()
#         current_string = ""
#         longest = 0
#         i = 0
#         while i < len(s):
#             if s[i] not in char_set:
#                 current_string += s[i]
#                 char_set[s[i]] = i
#                 i += 1
#             else:
#                 longest = len(current_string) if len(current_string) > longest else longest
#                 current_string = ""
#
#                 i = char_set[s[i]] + 1
#                 if i >= len(s):
#                     break
#
#                 char_set.clear()
#
#         longest = len(current_string) if len(current_string) > longest else longest
#         return longest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        char_set = set()
        lp = 0
        rp = 0
        longest = 0
        while rp < len(s):
            if s[rp] not in char_set:
                char_set.add(s[rp])
                longest = max(longest,len(char_set))
                rp += 1
            else:
                char_set.remove(s[lp])
                lp += 1
        return longest


my_solution = Solution()
print(my_solution.lengthOfLongestSubstring("abcabcbb"))
print(my_solution.lengthOfLongestSubstring("bbbb"))
print(my_solution.lengthOfLongestSubstring("pwwkew"))
print(my_solution.lengthOfLongestSubstring(""))
print(my_solution.lengthOfLongestSubstring(" "))
print(my_solution.lengthOfLongestSubstring("dvdf"))
print(my_solution.lengthOfLongestSubstring("au"))
print(my_solution.lengthOfLongestSubstring("tmmzuxt"))

