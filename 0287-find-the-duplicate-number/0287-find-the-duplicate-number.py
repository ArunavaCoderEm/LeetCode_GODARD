class Solution(object):
    def findDuplicate(self, nums):
        num = sorted(nums)
        for i in range (0,len(num)):
            if (num[i] == num[i+1]):
                return num[i]
        return None