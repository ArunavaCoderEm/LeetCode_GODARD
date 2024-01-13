class Solution(object):
    def singleNumber(self, nums):
        x = [i for i in nums if(nums.count(i) == 1)]
        return x[0]