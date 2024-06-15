class Solution:
    # thanks neetcode two heap concept
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        mp = []
        mc = [(co,pr) for co, pr in zip(capital,profits)]
        heapq.heapify(mc)
        for i in range(k):
            while(mc and mc[0][0] <= w):
                cs, pr = heapq.heappop(mc)
                heapq.heappush(mp, (-1*pr))
            if(not mp): break
            res = -1 * (heapq.heappop(mp))
            w += res
        return w