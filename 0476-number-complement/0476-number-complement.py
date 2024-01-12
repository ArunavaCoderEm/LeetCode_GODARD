class Solution(object):
    def findComplement(self, num):
        x = (bin(num).replace("0b",""))
        res = x.replace('1', '%temp%').replace('0', '1').replace('%temp%', '0')
        return int(res,2)
        