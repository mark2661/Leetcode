class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        self.mainCCount = [0] * 26
        self.CCount = [0] * 26
        self.result = []
        for c in p:
            self.mainCCount[ord(c) - ord("a")] += 1

        back = 0
        for c in range(len(p)-1):
            self.CCount[ord(s[c]) - ord("a")] += 1

        for i, c in enumerate(s[len(p)-1:]):
            self.CCount[ord(c) - ord("a")] += 1
            if self.CCount == self.mainCCount:
                self.result.append(i)
            self.CCount[ord(s[i]) - ord("a")] -= 1

        return self.result

my_solution = Solution()
print(my_solution.findAnagrams("abab", "ab"))