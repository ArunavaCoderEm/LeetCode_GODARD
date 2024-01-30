class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if(a == 1):
            return 1
        res = pow(a,int("".join(map(str,b))),1337)
        return res