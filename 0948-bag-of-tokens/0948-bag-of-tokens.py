class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        i,res,j,m = 0,0,len(tokens) - 1, 0
        tokens.sort()
        # sliding window
        while(i <= j):
            if(tokens[i] <= power):
                power -= tokens[i]
                i += 1
                res += 1
                m = max(m,res)
            elif(res > 0):
                power += tokens[j]
                j -= 1
                res -= 1
            elif(tokens[i] > power or res < 0): break
        return m