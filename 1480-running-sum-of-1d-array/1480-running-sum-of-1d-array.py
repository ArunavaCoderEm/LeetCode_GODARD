class Solution(object):
    def runningSum(self, nums):
        res = []
        summ = 0
        for i in nums:
            summ += i
            res.append(summ)
        return res