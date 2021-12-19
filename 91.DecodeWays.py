class Solution:
    def numDecodings(self, s):
        #special cases
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        self.s = s
        self.seen = set()
        return self.DFS(0)

    def DFS(self, pointer):
        def isValid(val):
            return 0 < int(val) < 27

        if pointer in self.seen:
            return 0
        if pointer == len(self.s):
            return 1
        self.seen.add(pointer)
        result = 0
        if isValid(self.s[pointer]):
            result += self.DFS(pointer + 1)
        if pointer < len(self.s) - 1 and isValid(self.s[pointer] + self.s[pointer + 1]):
            result += self.DFS(pointer + 2)
        return result




my_solution = Solution()
print(my_solution.numDecodings("10"))
print(my_solution.numDecodings("27"))
print(my_solution.numDecodings("12"))
print(my_solution.numDecodings("11106"))
print(my_solution.numDecodings("226"))
print(my_solution.numDecodings("1201234"))