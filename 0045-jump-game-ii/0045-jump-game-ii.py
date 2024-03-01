class Solution:
    def jump(self, nums: List[int]) -> int:
        c = 0
        res = 0
        for i in range(1, len(nums)):
            nums[i] = max(nums[i] + i, nums[i-1])
        while(c < len(nums) - 1):
            res += 1
            c = nums[c]
        return res