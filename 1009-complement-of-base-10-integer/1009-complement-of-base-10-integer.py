class Solution(object):
    def bitwiseComplement(self, n):
        x = bin(n).replace("0b","")
        res = x.replace('1', '%temp%').replace('0', '1').replace('%temp%', '0')
        return int(res,2)
        