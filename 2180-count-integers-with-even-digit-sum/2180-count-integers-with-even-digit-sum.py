def check(n):
    res = []
    if (len(str(n)) == 1 and n % 2 == 0):
        return True
    for j in range (len(str(n))):
        res.append(int(str(n)[j]))
    return (sum(res) % 2 == 0)
class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range (1,num+1):
            if(check(i)):
                count += 1
        return count