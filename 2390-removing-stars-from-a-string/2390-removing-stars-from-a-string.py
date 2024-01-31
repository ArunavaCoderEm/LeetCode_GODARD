class Solution:
    def removeStars(self, s: str) -> str:
        t,i = [],0
        while(i < len(s)):
            if(s[i] == "*"):
                t.pop()
            else:
                t += [s[i]]
            i += 1
        return ''.join(t)       