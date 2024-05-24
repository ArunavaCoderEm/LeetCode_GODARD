class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1
        res = []
        while(t <= b and l <= r):
            if(t <= b):
                for i in range(l, r + 1):
                    ele = matrix[t][i]
                    res.append(ele)
            t += 1
            if(l <= r):
                for i in range(t, b + 1):
                    ele = matrix[i][r]
                    res.append(ele)  
            r -= 1
            if(t <= b):
                for i in range(r,l-1,-1):
                    ele = matrix[b][i]
                    res.append(ele)
            b -= 1
            if(l <= r):
                for i in range(b,t-1,-1):
                    ele = matrix[i][l]
                    res.append(ele)   
            l += 1      
        return res