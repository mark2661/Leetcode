class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        self.ht = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }

        return self.DFS(digits)

    def DFS(self, digits):
        if len(digits) == 1:
            return self.ht[digits]
        first = digits[0]
        letters = self.ht[first]
        combinationWithoutLetters = self.DFS(digits[1:])
        combinationWithLetters = []

        for letter in letters:
            for combination in combinationWithoutLetters:
                combinationWithLetters.append(letter + combination)

        return combinationWithLetters

my_solution = Solution()
print(my_solution.letterCombinations("23"))
print(my_solution.letterCombinations(""))
print(my_solution.letterCombinations("2"))

