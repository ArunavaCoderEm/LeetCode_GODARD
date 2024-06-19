def countB(bloomDay,l,k):
    ans, j = 0, -1
    for i in range(len(bloomDay)):
        if (bloomDay[i] > l):
            j = i  
        elif (i-j == k):
            ans += 1
            j = i  
    return ans
# Like binary search find pivot
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if(m * k > len(bloomDay)): return -1
        le , ri = 0 , max(bloomDay)
        while(le < ri):
            mid = (le + (ri-le)//2)
            res = countB(bloomDay,mid,k)
            if(res >= m): ri = mid
            else: le = mid + 1
        return le