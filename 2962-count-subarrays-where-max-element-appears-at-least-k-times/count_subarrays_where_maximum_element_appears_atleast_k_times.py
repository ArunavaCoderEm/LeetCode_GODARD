# class Solution:
#     def countSubarrays(self, nums: List[int], k: int) -> int:
#         m = max(nums)
#         i = 0
#         j = i + 1
#         count = 0
#         while(i < len(nums)):
#             if(nums[i:j].count(m) >= k):
#                 count += 1
#                 j += 1
#             else: j += 1
#             if(j > len(nums)):
#                 i += 1
#                 j = i + 1
#         return count

## Second method 
## both uses sliding window concept

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        i = 0
        j = 0
        count = 0
        res = 0
        while(j < len(nums)):
            if(nums[j] == m):
                count += 1
            while(count >= k):
                if(nums[i] == m): count -= 1
                i += 1
                res += len(nums) - j
            j += 1
        return res
