class Solution:
    ## Brute Force mayBEE (Its 2 am)
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        maxx = -69
        for i in range(len(heights)):
            res,l,r = heights[i],heights[i],heights[i]
            for j in range(i+1, len(heights)):
                l = min(l,heights[j])
                res += l
            for k in range(i-1, -1, -1):
                r = min(r,heights[k])
                res += r
            maxx = max(maxx, res)
        return maxx