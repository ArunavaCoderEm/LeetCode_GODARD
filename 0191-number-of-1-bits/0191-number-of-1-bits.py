class Solution(object):
    def hammingWeight(self, n):
        x = bin(n).replace("0b","")
        return x.count("1")