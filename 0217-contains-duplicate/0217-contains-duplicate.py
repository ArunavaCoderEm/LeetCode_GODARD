class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        if (len(nums) <= 1):
            return False
        for i in range (0,len(nums)-1):
            if (nums[i] == nums[i+1]):
                return True
        return False
        