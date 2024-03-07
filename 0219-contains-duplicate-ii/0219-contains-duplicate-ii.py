class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c = {}
        for i in range(len(nums)):
            if (nums[i] in c):
                if (abs(c[nums[i]] - i) <= k): return True
            c[nums[i]] = i
        return False