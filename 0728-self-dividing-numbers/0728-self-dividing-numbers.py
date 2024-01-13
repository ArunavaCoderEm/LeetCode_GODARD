def check(n):
    res = []
    for i in str(n):
        if ("0" not in str(i)):
            if (int(n)%int(i) == 0):
                res.append(0)
            else:
                res.append(1)
    return sum(res) == 0 

class Solution(object):
    def selfDividingNumbers(self, left, right):
        res = []
        for i in range (left,right+1):
            if (check(i) and "0" not in str(i)):
                res.append(i)
        return res