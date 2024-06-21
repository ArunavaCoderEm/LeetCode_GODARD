class Solution(object):
    ## ezz sliding window imp on 2nd loop
    def maxSatisfied(self, customers, grumpy, minutes):
        chk, res, ans = 0, 0, 0
        for i in range(len(customers)):
            if (grumpy[i] == 0):
                chk += customers[i]
            elif (i < minutes):
                ans += customers[i]
        res = ans
        for i in range(minutes, len(customers)):
            ans += (customers[i] * grumpy[i])
            ans -= (customers[i - minutes] * grumpy[i - minutes])
            res = max(res, ans)
        return chk + res       