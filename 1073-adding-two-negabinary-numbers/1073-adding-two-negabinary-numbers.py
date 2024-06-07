def conv(n,b):
    c = 0
    s = 0
    for i in range(len(n) - 1, -1,-1):
        res = n[i] * (b ** c)
        s += res
        c += 1
    return s
def convback(arr,n,b):
    while(True):
        r = n % b
        n = n // b
        if(r < 0):
            r += 2
            n += 1
        arr.append(r)
        if(n == 0): break
    arr.reverse()
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res1 = conv(arr1,-2)
        res2 = conv(arr2,-2)
        res = res1 + res2
        ans = []
        print(res1,res2,res)
        convback(ans,res,-2)
        return ans