class Solution:
    #EASY PROBLEM EASY SOLN
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        curr,count = 0,0
        banned = set(banned)
        for i in range (1,n+1):
            if (i not in banned and curr + i <= maxSum):
                count += 1
                curr += i
        return count
       