class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l = 0
        r = n - 1
        t = 0
        count = 1
        b = n - 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        while(t <= b and l <= r):
            for i in range(l, r + 1):
                res[t][i] = count
                count += 1
            t += 1
            for i in range(t, b + 1):
                res[i][r] = count
                count += 1
            r -= 1
            for i in range(r,l-1,-1):
                res[b][i] = count
                count += 1
            b -= 1
            for i in range(b,t-1,-1):
                res[i][l] = count
                count += 1
            l += 1
        return res