class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cita = sorted(citations,reverse = True)
        res = 0
        for i,j in enumerate(cita):
            if(j >= (i+1)): res = i + 1
            else: break
        return res