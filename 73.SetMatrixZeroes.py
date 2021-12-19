class Solution:
    def setZeroes(self, matrix):
        self.n = len(matrix[0])
        self.columnSet = set()
        self.rowSet = set()

        def setColumnsToZero():
            for row in range(len(matrix)):
                for column in self.columnSet:
                    matrix[row][column] = 0
        def setRowsToZero():
            for row in self.rowSet:
                matrix[row] = [0] * self.n

        for row in range(len(matrix)):
            foundZero = False
            for column in range(self.n):
                if matrix[row][column] == 0:
                    self.columnSet.add(column)
                    foundZero = True
            if foundZero:
                self.rowSet.add(row)
        setColumnsToZero()
        setRowsToZero()
        return matrix

my_solution = Solution()
print(my_solution.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))