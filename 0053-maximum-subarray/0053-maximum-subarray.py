class Solution:
    # Easiest sliding window approach
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = float('-inf')
        res = 0
        for i in nums:
            if(res < 0): res = 0
            res += i
            maxx = max(res,maxx)
        return maxx