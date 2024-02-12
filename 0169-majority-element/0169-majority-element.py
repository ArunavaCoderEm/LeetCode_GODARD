class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f = max(set(nums),key = nums.count)
        return f