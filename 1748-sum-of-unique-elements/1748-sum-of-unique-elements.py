class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        summ = 0
        for i in nums:
            if (nums.count(i) <= 1):
                summ += i
        return summ