class Solution:
    def reverseBits(self, n):
        y = bin(n).replace("0b","").rjust(32,"0")
        y = str(y)
        c = y[::-1]
        return int(c,2)