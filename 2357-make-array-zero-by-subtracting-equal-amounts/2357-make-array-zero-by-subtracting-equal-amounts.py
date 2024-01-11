class Solution(object):
    def minimumOperations(self, nums):
        x = set(nums) - {0}
        return len(x)
       