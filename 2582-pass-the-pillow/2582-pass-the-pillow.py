##  HOW the F it took 35 mins for me !!!!
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if (n < 1 or time < 1):
            return -1
        time = time % (2 * n - 2)
        if(time < n): return time + 1
        else: ans = 2 * n - time - 1
        return ans