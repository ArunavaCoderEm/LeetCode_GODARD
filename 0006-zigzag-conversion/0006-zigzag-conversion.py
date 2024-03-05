class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1):
            return s
        res = [''] * numRows
        check = 1 
        count = 0
        for i in range(len(s)):
            res[count] += s[i]
            if (count == 0):
                check = 1
            elif (count == numRows - 1):
                check = -1
            count += check
        return ''.join(res)