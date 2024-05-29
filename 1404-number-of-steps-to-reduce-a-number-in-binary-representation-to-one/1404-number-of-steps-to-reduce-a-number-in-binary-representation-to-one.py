def btd(n):
    return int(n,2)

def checkodd(n):
    return (n % 2 != 0)

class Solution:
    def numSteps(self, s: str) -> int:
        step = 0
        num = btd(s)
        while(num != 1):
            if(checkodd(num)): num += 1
            else: num //= 2
            step += 1
        return step