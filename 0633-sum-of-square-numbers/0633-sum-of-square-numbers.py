class Solution:
    # Easiest approach
    def judgeSquareSum(self, c: int) -> bool:
        res = int(c ** 0.5)
        i = 0
        j = res
        while(i <= j):
            if((i**2) + (j ** 2) == c): return True
            elif((i ** 2) + (j ** 2) < c):
                i += 1
            else:
                j -= 1
        return False