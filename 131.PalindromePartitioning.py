class Solution:
    def partition(self, s):
        if len(s) == 1:
            return [[s]]
        self.result = []
        self.s = s
        self.DFS(0,[])
        return self.result

    def DFS(self,start,currentList):
        def isPallindrome(start, end):
            while start < end:
                if self.s[start] != self.s[end]:
                    return False
                start += 1
                end -= 1
            return True

        if start >= len(self.s):
            self.result.append(currentList.copy())
            return
        for end in range(start, len(self.s)):
            if isPallindrome(start, end):
                currentList.append(self.s[start:end+1])
                self.DFS(end + 1, currentList)
                currentList.pop()

my_solution = Solution()
print(my_solution.partition("aab"))
