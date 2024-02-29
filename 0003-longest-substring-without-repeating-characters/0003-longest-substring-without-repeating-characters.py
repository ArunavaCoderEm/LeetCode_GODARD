class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 0): return len(s)
        if(len(s) != 0 and not s.strip()): return 1
        i = 0
        j = i + 1
        res = []
        while(i < len(s)):
            if(len(set(s[i:j])) == len(s[i:j])):
                res.append(s[i:j])
                j += 1
            else:
                i += 1
            if(j > len(s)):
                i += 1
                j = i + 1
        ret = sorted(res,key=len)
        return len(ret[len(ret) - 1])