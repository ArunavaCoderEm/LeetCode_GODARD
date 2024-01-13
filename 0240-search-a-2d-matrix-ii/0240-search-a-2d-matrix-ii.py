class Solution(object):
    def searchMatrix(self, matrix, target):
        col = len(matrix[0])
        row = len(matrix)
        for i in range(row):
            for j in range(col):
                if(matrix[i][j] == target):
                    return True
        return False
        