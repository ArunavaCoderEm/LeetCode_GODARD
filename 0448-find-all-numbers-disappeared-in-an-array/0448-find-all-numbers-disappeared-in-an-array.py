# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         res = []
#         for i in range (1,len(nums)+1):
#             if (i not in list(set(nums))):
#                 res.append(i)
#         return res

## ANY

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = set(nums)
        x = [i for i in range(1,len(nums)+1) if i not in res]
        return x