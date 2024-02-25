class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort() 
        if(len(nums) == 3 and sum(nums) == 0): return [nums]
        for val in range(0,len(nums)):
            if(nums[val] == nums[val - 1] and val > 0): continue
            i = val + 1
            target = 0
            j = len(nums) - 1
            while(i < j):
                if(nums[val] + nums[i] + nums[j] == target):
                    res.append([nums[val],nums[i],nums[j]])
                    i += 1
                    while(i < j and nums[i] == nums[i - 1]): i += 1
                if(nums[val] + nums[i] + nums[j] > target): j -= 1
                if(nums[val] + nums[i] + nums[j] < target): i += 1
        return res
        