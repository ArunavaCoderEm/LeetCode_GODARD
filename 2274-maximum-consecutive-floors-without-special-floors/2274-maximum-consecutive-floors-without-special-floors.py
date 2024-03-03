# class Solution:
#     def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
#         res = []
#         count = 0
#         for i in range(bottom,top+1):
#             if(i in special):
#                 res.append(count)
#                 count = 0
#             else:
#                 count += 1
#             if(i == top and i not in special): res.append(count)        
#         res.sort()
#         return res[len(res) - 1]

## second method
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        count = 0
        topp = float('-inf')
        special.sort()
        topp = max(topp,special[0] - bottom)
        for i in range(1,len(special)):
            count = special[i] - special[i-1] - 1
            topp = max(topp,count)
        res = max(topp,top - special[-1])
        return res
