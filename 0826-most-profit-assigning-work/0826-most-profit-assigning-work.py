# Thanks Bidhan Sir LOLL
# Greedy approach
# Still took time but ezzz
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        c = {}
        for i in range(len(difficulty)):
            c[difficulty[i]] = max(c.get(difficulty[i], 0), profit[i])
        ans = sorted(c.keys())
        works = sorted(worker)
        retres = 0
        k = 0
        ansres = 0
        for j in range(len(works)):
            while (k < len(ans) and ans[k] <= works[j]):
                retres = max(retres, c[ans[k]])
                k += 1
            ansres += retres
        return ansres