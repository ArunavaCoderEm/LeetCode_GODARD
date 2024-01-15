class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if(nums.count(i) == 1):
                res.append(i)
        return res