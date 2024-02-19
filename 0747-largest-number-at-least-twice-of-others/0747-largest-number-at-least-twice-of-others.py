class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if(nums[i] == max(nums)): continue
            if(2*nums[i] > max(nums)): return -1
        return nums.index(max(nums))