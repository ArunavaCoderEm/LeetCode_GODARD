from collections import defaultdict
## Just revised Classes in py !! I was a fool to do prblms like that before !
# this is the best process so far !!
class Solution:
    def __init__(self):
        self.idx = defaultdict(list)
    def checkfor(self, nums: List[int]):
        for i, j in enumerate(nums):
            self.idx[j].append(i)
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        self.checkfor(nums)      
        res = []
        ans = self.idx[x]
        for n in queries:
            if (n > len(ans)):
                res.append(-1)
            else:
                res.append(ans[n - 1])       
        return res
