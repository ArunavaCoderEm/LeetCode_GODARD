# # sliding window TLE NICE
# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         i = 0
#         j = i + 2
#         if(len(nums) == 1): return False
#         while(i < len(nums)):
#             if(sum(nums[i:j]) % k == 0 and len(nums[i:j]) >= 2): 
#                 return True
#             else : j += 1
#             if(j > len(nums)):
#                 i += 1
#                 j = i + 2
#         return False 

# DP table TLE NICE
# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         if(len(nums) < 2): return False
#         numsum = [0] * (len(nums) + 1)
#         for i in range(1, len(nums)+1):
#             numsum[i] = numsum[i-1] + nums[i-1]
#         print(numsum)
#         for j in range(len(nums) - 1):
#             for m in range(j+2, len(nums) + 1):
#                 if(numsum[m] - numsum[j]) % k == 0: return True
#         return False


# Let's not calculate sum only !! direct check remainder
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        res = {}
        summ = 0
        presum = 0
        for i in nums:
            summ += i
            rem = summ % k
            if(rem in res): return True
            res[presum] = rem
            presum = rem
        return False