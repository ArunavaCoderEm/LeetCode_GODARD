class Solution(object):
    def thirdMax(self,nums):
        if (len(list(set(nums))) >= 3):
            x = list(set(nums))
            x.sort()
            return x[len(x) - 3]
        else :
            return max(nums)    
            