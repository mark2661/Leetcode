
# def pascalsTriangle(n,previousline = [1,1],triangle = [[1],[1,1]], rowNum = 3):
#     if n == 0:
#         return []
#     if n == 1:
#         return [[1]]
#     if n == 2:
#         return [[1],[1,1]]
#
#     new_row = [1]
#     for i in range(len(previousline) - 1):
#         new_row.append(previousline[i] + previousline[i+1])
#     new_row.append(1)
#
#
#     triangle.append(new_row)
#
#     if rowNum == n:
#         return triangle
#     else:
#         return pascalsTriangle(n,new_row,triangle,rowNum + 1)


# class Solution:
#     def generate(self, numRows):
#         return pascalsTriangle(numRows)

class Solution:
    def generate(self, numRows):

        triangle = []

        for row_num in range(numRows):
            row = [None for _ in range(row_num + 1)]
            row[0],row[-1] = 1,1

            for i in range(1,len(row) - 1):
                row[i] = triangle[row_num-1][i-1] + triangle[row_num-1][i]

            triangle.append(row)

        return triangle


my_solution = Solution()
print(my_solution.generate(5))