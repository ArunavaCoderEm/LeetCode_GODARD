class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        res = skills[:]
        # use HM to keep track of wins
        ## this was a good question
        n = len(skills)
        if (k >= n - 1):
            return skills.index(max(skills))
        d = {skill: 0 for skill in skills}
        winL = res[0]
        chkw = 0
        while (chkw < k):
            x = res[0]
            y = res[1]
            if (x > y):
                res.remove(y)  
                res.append(y) 
                d[x] += 1
                chkw = d[x]
                winL = x
            else:
                res.remove(x) 
                res.append(x)  
                d[y] += 1
                chkw = d[y]
                winL = y
            if (chkw > 1):
                rem = k - chkw
                rep = len(res) - 1
                ans = rem // rep
                chkw += ans * rep
                d[winL] = chkw  
                if (chkw >= k):
                    break
        return skills.index(winL)