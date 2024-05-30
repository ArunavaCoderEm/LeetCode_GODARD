class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        for i in range(1,n+1):
            ans = str(i)
            if('3' in ans or '4' in ans or '7' in ans): continue
            if('2' in ans or '5' in ans or '6' in ans or '9' in ans): res += 1
        return res