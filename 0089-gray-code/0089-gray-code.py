class Solution:
    # # SIMPLE LEFT SHIFT
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(0,n):
            NresR = []
            for j in res:
                NresR.append(j+(1<<i))
            res = res+NresR[::-1]
        return res
        