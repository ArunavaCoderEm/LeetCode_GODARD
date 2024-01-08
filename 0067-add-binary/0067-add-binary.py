class Solution(object):
    def addBinary(self, a, b):
        z = int(a,2)
        x = int(b,2)
        summ = bin(z + x).replace("0b","")
        return str(summ)