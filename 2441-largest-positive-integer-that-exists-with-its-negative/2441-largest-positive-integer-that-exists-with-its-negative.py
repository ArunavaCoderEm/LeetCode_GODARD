class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if (-(i) in nums):
                res.append(abs(i))
        if(len(res) > 0):
            return max(res)
        return -1 