class Solution(object):
    def climbStairs(self,n):
        madearr = [0, 1]
        while (len(madearr) < n):
                madearr.append(madearr[-1] + madearr[-2])
        if (n == 1):
            return 1  
        return sum(madearr)+1

        