"""
Expansion around centre approach

loop through the string treating each character as the centre of a palindrome
keep expanding in both directions until either the leftmost and rightmost letters are not equal or the left or right pointer reaches the edge of the string
once expansion has stop return length of the palindrome and update if this is longer than the largest palindrome found so far.

Time complexity
looping through each 'centre' in the string -> O(n)
expansion algorithm -> O(n) and is performed on every centre
Therefore Overall -> O(n^2)
"""
# def expand_from_centre(s,left,right):
#     if s is None or left > right:
#         return 0
#     while left >= 0 and right < len(s) and s[left] == s[right]:
#         left -= 1
#         right += 1
#
#     return (right - left - 1) #returns length of extension from centre
#
#
# class Solution:
#     def longestPalindrome(self, s):
#
#         start = 0
#         end =0
#
#         for i in range(len(s)):
#             len_one = expand_from_centre(s, i, i) #odd length string (single character centre)
#             len_two = expand_from_centre(s, i, i+1) # even length string (double character centre)
#             length = max(len_one,len_two)
#             if length > (end - start):
#                 start = i - ((length - 1) // 2) #index for start of palindrome
#                 end = i + (length // 2) #index for end of palindrome
#         return s[start:(end + 1)]
#
#         #return start
#
#
# my_solution = Solution()
# print(my_solution.longestPalindrome("babad"))


"""
Dynamic Programming approach
Geeks 4 Geeks Video and article
https://www.youtube.com/watch?v=TLaGwTnd3HY
https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/

Additional video
https://www.youtube.com/watch?v=UflHuQj6MVA

Time complexity -> O(n^2)

"""
class Solution:

    def longestPalindrome(self, s):

        n = len(s)
        dp =  [[0 for x in range(n)] for x in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for d in range(2, n+1): #d = distance between pointers ?
            for i in range(n-d+1): # i = trailing pointer
                j = i + d - 1 # j = leading pointer
                if(s[i] == s[j] and d == 2):
                    dp[i][j] = 2
                elif(s[i] == s[j] and dp[i+1][j-1] > 0):
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i+1][j])

        return max(map(max,dp))

my_solution = Solution()
print(my_solution.longestPalindrome("babcbab"))
