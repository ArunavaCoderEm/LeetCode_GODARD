class Solution:
    ## EASIEST SOLUTION MAYBE
    def balancedStringSplit(self, s: str) -> int:
        c,bal = 0,0
        for i in range(0,len(s)):
            if(s[i] == 'L'): c += 1
            else: c -= 1
            if(c == 0): bal += 1
        return bal 