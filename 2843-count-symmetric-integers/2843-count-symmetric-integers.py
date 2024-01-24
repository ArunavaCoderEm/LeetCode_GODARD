class Solution:
    def countSymmetricIntegers(self,low: int, high: int) -> int:
        count = 0
        for i in range (low, high + 1):
            res1 = [int(str(i)[j]) for j in range (0,len(str(i))//2)]
            res2 = [int(str(i)[k]) for k in range (len(str(i))//2 , len(str(i)))]
            if(sum(res1) == sum(res2) and len(str(i)) % 2 == 0):
                count += 1
        return count
            