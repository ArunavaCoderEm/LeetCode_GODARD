class Solution:
    # brute force easy
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        mx = max(nums)
        if(mx < len(nums)): res += 1
        if(nums[0] != 0 and mx < len(nums)): res += 1
        for i in range(len(nums)):
            if(i + 1 > nums[i] and i + 1 < nums[-1] and i + 1 < nums[i + 1]):
                res += 1
        return res