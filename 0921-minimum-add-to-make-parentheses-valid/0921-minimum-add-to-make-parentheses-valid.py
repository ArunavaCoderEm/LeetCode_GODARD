class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if (not len(s)): return 0

        bracs, notvalid = 0, 0
        for i in range (len(s)):
            if(s[i] == '('): bracs += 1
            elif(s[i] != '(' and bracs > 0): bracs -= 1
            elif(s[i] != '(' and bracs <= 0): notvalid += 1

        res = bracs + notvalid
        return res
