# class Solution:
#     #Sliding window BrFo
#     def subarraysDivByK(self, nums: List[int], k: int) -> int:
#         c = 0
#         i = 0
#         j = i + 1
#         if(len(nums) == 1 and nums[0] % k != 0): return 0
#         while(i < len(nums)):
#             if(sum(nums[i:j]) % k == 0):
#                 c += 1
#             j += 1
#             if(j > len(nums)):
#                 i += 1
#                 j = i + 1
#         return c

# Better approach prefix sum
# keep track of remainders in HM
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remhm = {0 : 1}
        res = 0
        presum = 0
        for i in nums:
            presum += i
            rem = presum % k
            if(rem < 0): rem += k
            if(rem in remhm):
                res += remhm[rem]
                remhm[rem] += 1
            else: remhm[rem] = 1
        return res