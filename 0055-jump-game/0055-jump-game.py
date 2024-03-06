class Solution:
    def canJump(self, nums: List[int]) -> bool:
        c = nums[0]
        for i,j in enumerate(nums):
            if(c >= len(nums) - 1): return True
            if(j == 0 and c == i): return False
            if(j + i > c): c = i + j
        return True
        