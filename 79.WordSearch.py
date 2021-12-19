class Solution:
    def exist(self, board, word):
        self.board = board
        self.word = word
        self.column_total = len(board[0])
        self.row_total = len(board)
        valid = False

        for row in range(self.row_total):
            for column in range(self.column_total):
                valid = valid or self.explore(row, column, 0)

        return valid


    def explore(self, row, column, idx):

        if idx == len(self.word) - 1:
            return self.board[row][column] == self.word[idx]

        if self.board[row][column] != self.word[idx]:
            return False

        val = self.board[row][column]
        self.board[row][column] = "1"

        valid = False
        if self.validUp(row, column):
            valid = valid or self.explore(row - 1, column, idx + 1)
        if self.validDown(row, column):
            valid = valid or self.explore(row + 1, column, idx + 1)
        if self.validLeft(row, column):
            valid = valid or self.explore(row, column - 1, idx + 1)
        if self.validRight(row, column):
            valid = valid or self.explore(row, column + 1, idx + 1)

        self.board[row][column] = val
        return valid

    def validUp(self, row, column):
        return row - 1 >= 0
        
    def validDown(self, row, column):
        return row + 1 < self.row_total

    def validLeft(self, row, column):
        return column - 1 >= 0

    def validRight(self, row, column):
        return column + 1 < self.column_total

my_solution = Solution()
print(my_solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(my_solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(my_solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(my_solution.exist([["a","b"],["c","d"]], "cdba"))
print(my_solution.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))