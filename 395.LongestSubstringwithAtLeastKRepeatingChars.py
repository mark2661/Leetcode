class Solution:
    def longestSubstring(self, s, k):
        return self.longestSubStringWithK(s,k)

    def longestSubStringWithK(self,s,k):
        def find_mid(ht, s):
            for i in range(len(s)):
                if ht[s[i]] < k:
                    return i
            return -1

        if len(s) < k:
            return 0
        ht = {chr(ord('a') + i): 0 for i in range(26)}

        for char in s:
            ht[char] += 1

        mid = find_mid(ht, s)
        if mid == -1:
            return len(s)
        else:
            return max(self.longestSubStringWithK(s[:mid], k), self.longestSubStringWithK(s[mid+1:],k))


my_solution = Solution()
print(my_solution.longestSubstring("aaabb",3))
print(my_solution.longestSubstring("ababbc",2))
print(my_solution.longestSubstring("ababcabaaadc",2))