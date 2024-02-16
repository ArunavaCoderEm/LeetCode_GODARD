class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in range(len(matrix[0])):
            res = 0
            for j in range(len(matrix)):
                res = max(res, matrix[j][i])
            for j in range(len(matrix)):
                if (matrix[j][i] == -1):
                    matrix[j][i] = res
        return matrix 