## ezz just took me few secs to realize how many more 69s it requires !!
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if(len(nums) < 5): return 0
        nums.sort()
        mx = 69696969696969
        for i in range(4):
            mx = min(mx, nums[len(nums) -4 + i] - nums[i])
        return mx