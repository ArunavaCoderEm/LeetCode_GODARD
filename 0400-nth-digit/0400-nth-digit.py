class Solution:
    def findNthDigit(self, n: int) -> int:
        res1,res2,res3=1,1,10
        while (res3 < n):
            res1,res2 = res3, res2+1,
            res3 = res1+9*res2*(10**(res2-1))
        return int(str((10**(res2-1))+((n-res1)//(res2)))[(n-res1)%(res2)])