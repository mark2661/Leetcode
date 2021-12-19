class Solution:
    def letterCasePermutation(self, s):
        self.result = []
        self.word = s
        self.backtrack(0, s)
        return self.result


    def backtrack(self, idx, path):
        if idx >= len(self.word):
            self.result.append(path)
            return
        found = False
        while idx < len(self.word):
            if path[idx].isalpha():
                found = True
                if path[idx].islower():
                    path_with_capital = path[:idx] + path[idx].upper() + path[idx + 1:]
                else:
                    path_with_capital = path[:idx] + path[idx].lower() + path[idx + 1:]
                break
            idx += 1
        self.backtrack(idx + 1, path)
        if found:
            self.backtrack(idx + 1, path_with_capital)

my_solution = Solution()
print(my_solution.letterCasePermutation("a1b2"))
print(my_solution.letterCasePermutation("3z4"))
print(my_solution.letterCasePermutation("12345"))
print(my_solution.letterCasePermutation("0"))
print(my_solution.letterCasePermutation("C"))