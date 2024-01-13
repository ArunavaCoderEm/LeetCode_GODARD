class Solution(object):
    def digitCount(self, num):
        res = []
        for i in range(len(num)):
            if(int(num.count(str(i))) == int(num[i])):
                res.append(0)
            else:
                res.append(1)
        return sum(res) == 0
        