class Solution:
    def scoreOfString(self, s: str) -> int:
        summ = 0
        for i in range(1,len(s)):
            x = ord(s[i-1])
            y = ord(s[i])
            diff = abs(x-y)
            summ += diff
        return summ