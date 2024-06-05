class Solution:
    # just implement set that's it !!
    def partitionString(self, s: str) -> int:
        count = 0
        res = set()
        for i in range(len(s)):
            if(s[i] in res):
                count += 1
                res = set()
                res.add(s[i])
            else: res.add(s[i])
            if(i >= len(s) - 1): 
                count += 1
                return count
        return count