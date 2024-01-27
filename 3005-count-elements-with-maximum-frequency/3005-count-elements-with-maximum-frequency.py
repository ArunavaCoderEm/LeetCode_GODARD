class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = 0
        c = Counter(nums)
        val = max(c.values())
        for i in c.values():
            if(i == val):
                count += val
        return count