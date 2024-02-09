class Solution:
    ## easy sliding window
    def countSubstrings(self,s: str) -> int:
        i,j,count = 0,1,0
        while(i < len(s)):
            if(s[i:j] == s[i:j][::-1]):
                count += 1
                j += 1
            else:
                j += 1
            if(j > len(s)):
                i += 1
                j = i + 1
        return count
        