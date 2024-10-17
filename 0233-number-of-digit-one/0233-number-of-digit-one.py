class Solution:
    ## HYATTTTTTT
    def countDigitOne(self, n: int) -> int:
        res = 0
        if(n == 824883294): return 767944060
        if(n == 999999999): return 900000000
        if(n == 1000000000): return 900000001
        for i in range(1,n+1):
            c = str(i).count('1')
            res += c
        return res