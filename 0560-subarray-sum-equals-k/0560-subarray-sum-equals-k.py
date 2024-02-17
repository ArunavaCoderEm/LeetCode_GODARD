from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)
        c[0] = 1
        ans,res = 0,0
        for i in range(len(nums)):
            res += nums[i]
            ans += c[res - k]
            c[res] += 1
        return ans