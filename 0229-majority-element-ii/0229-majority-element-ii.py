class Solution(object):
    def majorityElement(self, nums):
        nby3 = len(nums)//3
        res = []
        for i in list(set(nums)):
            if (nums.count(i) > nby3):
                res.append(i)
        return res