## I did it dirty but I guess there must be some formula
## to get ans without solving

def issafe(board, row, col, n):
    j = 0
    while j < col:
        if (board[row][j]): return False
        j += 1

    i = row
    j = col
    while (i >= 0 and j >= 0):
        if board[i][j]: return False
        i -= 1
        j -= 1
    
    i = row
    j = col
    while (j >= 0 and i < n):
        if board[i][j]: return False
        i += 1
        j -= 1
    
    return True

def solveQutil(board, col, n, finalres):
    if (col >= n): 
        finalres.append(["".join('Q' if board[i][j] else '.' for j in range(n)) for i in range(n)])
        return
    for i in range(n):
        if (issafe(board, i, col, n)):
            board[i][col] = 1
            solveQutil(board, col+1, n, finalres)
            board[i][col] = 0

def solver(n):
    board = [[0]*n for _ in range(n)]
    res = []
    solveQutil(board, 0, n, res)
    return res
    

class Solution:
    def totalNQueens(self, n: int) -> int:
        if(n == 1): return 1
        x = solver(n)
        return len(x)