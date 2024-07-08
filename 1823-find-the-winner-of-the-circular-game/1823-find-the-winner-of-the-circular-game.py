## Ezz only !!

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if (n == 0 or k == 0): return 0
        fr = [i for i in range(1,n+1)]
        st = 0
        size = n
        while(size > 1):
            st = (st + k -1) % size
            print(st)
            fr.pop(st)
            print(fr)
            size -= 1
        return fr[0]