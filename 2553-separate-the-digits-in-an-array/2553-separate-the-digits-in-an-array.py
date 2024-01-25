class Solution(object):
    def separateDigits(self, nums):
        res = []
        for i in nums:
            for j in range (len(str(i))):
                res.append(int(str(i)[j]))
        return res
        