# class Solution(object):
#     def missingNumber(self, nums):
#         minn = min(nums)
#         maxx = len(nums)
#         for i in range (minn, maxx + 1):
#             if (i not in nums):
#                 return i
#         return 0

## THANKS TO HACKERRANK
class Solution(object):
    def missingNumber(self, nums):
        summ = (len(nums)*(len(nums) + 1)) // 2;
        return summ - sum(nums)