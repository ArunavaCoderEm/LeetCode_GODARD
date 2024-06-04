class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = 9
        col = 9
        for i in range(row):
            res = set()
            for j in range(col):
                if(board[i][j] in res): return False
                elif(board[i][j] not in res and board[i][j] != '.'): res.add(board[i][j])
        for i in range(row):
            res = set()
            for j in range(col):
                if(board[j][i] in res): return False
                elif(board[j][i] not in res and board[j][i] != '.'): res.add(board[j][i])
        boxes = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for k,l in boxes:
            ans = set()
            for r in range(k,k+3):
                for c in range(l,l+3):
                    if(board[r][c] in ans): return False
                    elif(board[r][c] != '.'): ans.add(board[r][c])
        return True
        