class Solution:
    # easiest prefix sum straight forward
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        mod = (10**9) + 7
        res = [1]*n
        presum = [1]*(n)
        j = 0
        while(j < k):
            for i in range(1,n):
                presum[i] = res[i] + presum[i-1]
            res = presum
            j += 1
        ansp = presum[-1]
        ans = ansp % mod
        return ans