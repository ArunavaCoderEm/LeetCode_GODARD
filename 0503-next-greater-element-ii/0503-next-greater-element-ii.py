class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n

        if (len(set(nums)) == 1): return res

        for i in range(n):
            for j in range(1, n):
                if (nums[i] < nums[(i + j) % n]):
                    res[i] = nums[(i + j) % n]
                    break

        return res