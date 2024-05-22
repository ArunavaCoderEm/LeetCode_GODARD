class Solution:
    def tribonacci(self, n: int) -> int:
        n1 = 0
        n2 = 1
        n3 = 1
        for i in range(n):
            n4 = n1 + n2 + n3
            n1 = n2
            n2 = n3
            n3 = n4
        return n1