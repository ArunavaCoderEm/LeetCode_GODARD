#### Nice problem - XOR and prefix sum and iterate all acc to k
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_count = 0
        flipped = [0] * n 
        flip = 0  
        for i in range(n):
            if (i >= k):
                flip ^= flipped[i - k] 
            if (flip % 2 == nums[i]):
                if (i + k > n):
                    return -1  
                flip ^= 1
                flip_count += 1
                if (i + k < n):
                    flipped[i] = 1  
        return flip_count