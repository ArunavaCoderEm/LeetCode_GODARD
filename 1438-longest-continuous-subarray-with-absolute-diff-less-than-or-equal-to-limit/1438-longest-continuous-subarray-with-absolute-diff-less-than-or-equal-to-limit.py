## bisect inserts sorted way
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        i = 0
        res = []
        for j in range(n):
            bisect.insort(res,nums[j])
            if (res[-1] - res[0] > limit):
                res.pop(bisect.bisect(res,nums[i])-1)
                i += 1
        return (j-i+1)