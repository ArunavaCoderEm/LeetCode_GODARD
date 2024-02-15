class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:        
        res = 1
        c = 1
        for i in range(1, len(nums)):
            if (nums[i] == nums[i-1]):
                c += 1
            else:
                c = 1
            if (c <= 2):
                nums[res] = nums[i]
                res += 1      
        return res