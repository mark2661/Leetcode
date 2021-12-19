
def pascalsTriangle(n,previousline = [1,1], rowNum = 2):
    if n == 0:
        return [1]
    if n == 1:
        return [1,1]

    new_row = [1]
    for i in range(len(previousline) - 1):
        new_row.append(previousline[i] + previousline[i+1])
    new_row.append(1)


    if rowNum == n:
        return new_row
    else:
        return pascalsTriangle(n,new_row,rowNum + 1)



class Solution:
    def getRow(self, rowIndex):
        return pascalsTriangle(rowIndex)


my_solution = Solution()
print(my_solution.getRow(3))