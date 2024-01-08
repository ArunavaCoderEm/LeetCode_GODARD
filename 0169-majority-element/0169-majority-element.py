class Solution(object):
    def majorityElement(self, nums):
        c = []
        num = list(set(nums))
        for i in num:
            c.append(nums.count(i))
        for j in (num):
            if (nums.count(j) == max(c)):
                return j
        