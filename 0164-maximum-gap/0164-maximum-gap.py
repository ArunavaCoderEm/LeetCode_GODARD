class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if(len(nums) < 2): return 0
        res = []
        nums.sort()
        i = 0
        j = i + 1
        while(i < len(nums) - 1):
            res.append(abs(nums[i] - nums[j]))
            i += 1
            j += 1
        res.sort()
        return res[len(res) - 1]