class Solution:
    # first thing sorted (make it) array and placing
    # first intution binary search 
    def maxDistance(self, p: List[int], m: int) -> int:
        p.sort()
        res = -1
        l = 1 # as array val can't start from 0
        h = abs(p[-1] - p[0])
        while(l <= h):
            mid = (l + (h-l) // 2) # basic BS
            chpo = p[0]
            placed = 1
            for i in range(1,len(p)):
                if(p[i] - chpo >= mid):
                    chpo = p[i]
                    placed += 1 # if can be placed
            # if not
            if(placed >= m):
                res = mid # place update there
                l = mid + 1
            else: h = mid - 1 # basic BS
        return res
        