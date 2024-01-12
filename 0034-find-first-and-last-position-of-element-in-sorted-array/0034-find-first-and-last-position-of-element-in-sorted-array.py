class Solution(object):
    def searchRange(self, nums, target):
        if (target not in nums):
            return [-1,-1]
        elif (nums.count(target) == 1):
            x1 = (nums.index(target))
            return [x1,x1]
        elif (nums.count(target) == len(nums)):
            return [0,len(nums)-1]
        else:
            c = []
            x = (nums.index(target))
            c.append(x)
            nums.reverse()
            y = len(nums) - 1 - (nums.index(target))
            c.append(y)
            return c