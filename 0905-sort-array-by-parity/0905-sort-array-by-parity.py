class Solution(object):
    def sortArrayByParity(self, nums):
        c = []
        d = []
        for i in nums:
            if (i % 2 == 0):
                c.append(i)
            else :
                d.append(i)
        retnums = c+d
        return retnums
        