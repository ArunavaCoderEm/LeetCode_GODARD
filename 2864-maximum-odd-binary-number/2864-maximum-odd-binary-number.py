class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        x = s.count('1')
        l = s.count('0')
        res = '1'*(x-1) + '0'*l + '1'
        return res